#!/usr/bin/env python3
"""Find publications missing from _bibliography/publications.bib.

Queries OpenAlex for Anna Scaglione's recent work, discards anything that is
already present, is not a publication, or belongs to the *other* Anna
Scaglione (a medical researcher whose work contaminates the OpenAlex profile),
and writes any survivors as BibTeX.

Outputs:
  new_entries.bib  - BibTeX for entries confident enough to add
  report.md        - human-readable summary, including items NOT added

Deliberately conservative: when a decision is uncertain the entry is reported
rather than added, because a wrong entry on a public page is worse than a
missing one.
"""
import json, re, sys, unicodedata, urllib.parse, urllib.request
from datetime import date, timedelta

OPENALEX_AUTHOR = "A5029881017"
MAILTO = "scaglione.anna@gmail.com"
BIB = "_bibliography/publications.bib"
LOOKBACK_DAYS = 550
MATCH_THRESHOLD = 0.62          # token-set Jaccard; below this counts as "new"

# the other Anna Scaglione publishes in medicine
MEDICAL_VENUE = re.compile(
    r"molecular therapy|journal of clinical|current psychology|clinical medicine|"
    r"cardiovascular|cardiac|surgery|oncolog|immunolog|gene therapy|haematolog|"
    r"hematolog|nursing|psychiatr", re.I)
MEDICAL_TOPIC = re.compile(
    r"pericardial|retroviral|cardiac surgery|burnout|cognitive fusion|dyspnea|"
    r"immunomagnetic|vector purification|patients?\b|clinical trial", re.I)
# education material and recordings: real output, but not bibliography entries.
# These belong under "Beyond the classroom" on the teaching page.
EDUCATION_VENUE = re.compile(r"resource center|educational? resource|webinar|tutorial series", re.I)
# things OpenAlex/Scholar index as papers that are not papers
NOT_A_PAPER = re.compile(
    r"^(cartoon|humor|errata|corrigend|front matter|table of contents|"
    r"technical program|message from|committee|conference organization|"
    r"from the editor|advertis|list of reviewers|author index|welcome)", re.I)
STOP = {"the","and","for","with","via","using","from","ieee","proc","proceedings",
        "conference","vol","its","not","a","an","of","on","in","to"}

def norm_words(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii","ignore").decode().lower()
    return {w for w in re.sub(r"[^a-z0-9 ]", " ", s).split() if len(w) > 2 and w not in STOP}

def jaccard(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": f"sinelab-pubcheck ({MAILTO})"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return json.load(r)

def load_bib(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    entries = [e for e in re.split(r"\n(?=@)", text) if e.strip().startswith("@")]
    titles = [norm_words(m.group(1)) for e in entries
              for m in [re.search(r"title=\{(.*?)\}\s*,", e, re.S)] if m]
    keys = {re.match(r"@\w+\{([^,]+)", e.strip()).group(1) for e in entries}
    return titles, keys

def fmt_authors(authorships):
    out = []
    for a in authorships:
        name = (a.get("author") or {}).get("display_name") or ""
        name = name.strip()
        if not name:
            continue
        parts = name.split()
        if len(parts) == 1:
            out.append(parts[0])
        else:
            out.append(f"{parts[-1]}, {' '.join(parts[:-1])}")
    return " and ".join(out)

def bib_key(authorships, year, title, used):
    surname = "anon"
    if authorships:
        n = (authorships[0].get("author") or {}).get("display_name") or ""
        if n.split():
            surname = n.split()[-1]
    surname = re.sub(r"[^a-z]", "", unicodedata.normalize("NFKD", surname)
                     .encode("ascii","ignore").decode().lower()) or "anon"
    word = next((w for w in norm_words(title)), "paper")
    base = f"{surname}{year}{word}"
    key, n = base, 0
    while key in used:
        n += 1
        key = f"{base}{chr(96+n)}"
    used.add(key)
    return key

def entry_type(work, venue):
    t = work.get("type") or ""
    if re.search(r"magazine", venue, re.I):
        return "magazine"
    if t == "preprint" or re.search(r"arxiv|techrxiv|preprint", venue, re.I):
        return "preprint"
    if t in ("proceedings-article", "proceedings"):
        return "inproceedings"
    if t in ("book-chapter",):
        return "incollection"
    return "article"

def main():
    since = (date.today() - timedelta(days=LOOKBACK_DAYS)).isoformat()
    url = ("https://api.openalex.org/works?filter=author.id:"
           f"{OPENALEX_AUTHOR},from_publication_date:{since}"
           f"&per-page=200&mailto={urllib.parse.quote(MAILTO)}")
    works = get(url).get("results", [])
    bib_titles, used_keys = load_bib(BIB)

    added, skipped, flagged = [], [], []
    seen_new = []
    for w in works:
        title = (w.get("title") or "").strip()
        year = w.get("publication_year")
        loc = (w.get("primary_location") or {}).get("source") or {}
        venue = loc.get("display_name") or ""
        if not title:
            continue
        if not year:
            skipped.append((title, venue, "no year")); continue
        if MEDICAL_VENUE.search(venue) or MEDICAL_TOPIC.search(title):
            skipped.append((title, venue, "looks like the other A. Scaglione (medical)")); continue
        if NOT_A_PAPER.search(title):
            skipped.append((title, venue, "not a publication")); continue
        if EDUCATION_VENUE.search(venue):
            skipped.append((title, venue,
                "education resource, not a publication - belongs on the teaching page")); continue

        tw = norm_words(title)
        best = max((jaccard(tw, bt) for bt in bib_titles), default=0.0)
        if best >= MATCH_THRESHOLD:
            continue                                    # already in the bibliography
        dup = max((jaccard(tw, s) for s in seen_new), default=0.0)
        if dup >= MATCH_THRESHOLD:
            skipped.append((title, venue, "duplicate of another new item (preprint/published pair)")); continue

        etype = entry_type(w, venue)
        if etype == "preprint" and not venue:
            venue = "arXiv preprint"
        if 0.45 <= best < MATCH_THRESHOLD:
            flagged.append((title, venue, year, round(best, 2)))
            continue                                    # close to something we have: report, do not add

        seen_new.append(tw)
        fields = [("title", title)]
        au = fmt_authors(w.get("authorships") or [])
        if au: fields.append(("author", au))
        if etype == "inproceedings":   fields.append(("booktitle", venue))
        elif etype == "incollection":  fields.append(("booktitle", venue))
        elif venue:                    fields.append(("journal", venue))
        bib = w.get("biblio") or {}
        for src, dst in (("volume","volume"), ("issue","number")):
            if bib.get(src): fields.append((dst, bib[src]))
        if bib.get("first_page") and bib.get("last_page"):
            fields.append(("pages", f"{bib['first_page']}--{bib['last_page']}"))
        fields.append(("year", str(year)))
        if w.get("doi"):
            fields.append(("note", w["doi"].replace("https://doi.org/", "doi:")))
        key = bib_key(w.get("authorships") or [], year, title, used_keys)
        body = ",\n".join(f"  {k}={{{v}}}" for k, v in fields)
        added.append((key, f"@{etype}{{{key},\n{body}\n}}", title, venue, year))

    with open("new_entries.bib", "w", encoding="utf-8") as fh:
        fh.write("\n\n".join(a[1] for a in added) + ("\n" if added else ""))

    with open("report.md", "w", encoding="utf-8") as fh:
        fh.write(f"OpenAlex returned **{len(works)}** works since {since}.\n\n")
        if added:
            fh.write(f"### {len(added)} entries added in this PR\n\n")
            for key, _, title, venue, year in added:
                fh.write(f"- **{title}**  \n  {venue or '(no venue)'} · {year} · `{key}`\n")
            fh.write("\n")
        if flagged:
            fh.write(f"### {len(flagged)} similar to something already listed — NOT added, please check\n\n")
            for title, venue, year, score in flagged:
                fh.write(f"- **{title}**  \n  {venue or '(no venue)'} · {year} · similarity {score}\n")
            fh.write("\n")
        if skipped:
            fh.write(f"<details><summary>{len(skipped)} discarded</summary>\n\n")
            for title, venue, why in skipped:
                fh.write(f"- {title[:90]} — _{why}_\n")
            fh.write("\n</details>\n")
        fh.write("\nSource: OpenAlex. Every entry is machine-generated — check before merging.\n")

    print(f"added={len(added)} flagged={len(flagged)} skipped={len(skipped)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
