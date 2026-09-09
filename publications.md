---
title: Publication
permalink: /research/publication/
---

For those interested in numbers, see Anna's [google scholar citations profile](https://scholar.google.com/citations?user=Z43BgdEAAAAJ&hl=en).

We try to include links for all of our papers. Some of the links open PDFs, others direct you to a journal's site where that particular publication is available for download. If you cannot access one of our papers, let us know. The copyright notice for these papers is listed at the bottom of the page.

<hr>

<div id="pubindex"></div>

{% bibliography --max 5 %}


<style>
#pubindex{margin:.2rem 0 1.6rem;font-family:"Open Sans","Helvetica Neue",Helvetica,sans-serif}
#pubindex .chip{display:inline-block;margin:0 .35rem .45rem 0;padding:.26rem .6rem;border:1px solid #e0e0e0;
  border-radius:999px;font-size:.68rem;color:#444;cursor:pointer;background:#fff;transition:all .13s ease;
  text-transform:uppercase;letter-spacing:.03em}
#pubindex .chip:hover{border-color:#AA162C;color:#AA162C}
#pubindex .chip b{font-weight:700;color:#AA162C;margin-left:.3rem}
#pubindex .allbtn{border-style:dashed;color:#777}
details.pubcat{border-top:1px solid #eee;margin:0}
details.pubcat>summary{cursor:pointer;list-style:none;padding:.7rem .2rem;font-family:"Open Sans",sans-serif;
  font-size:.9rem;font-weight:600;color:#333;display:flex;align-items:baseline;gap:.5rem}
details.pubcat>summary::-webkit-details-marker{display:none}
details.pubcat>summary:hover{color:#AA162C}
details.pubcat>summary::before{content:"\25B8";color:#AA162C;font-size:.72rem;transition:transform .15s ease}
details.pubcat[open]>summary::before{content:"\25BE"}
details.pubcat>summary .n{margin-left:auto;font-size:.72rem;font-weight:400;color:#999}
details.pubcat[open]>summary{border-bottom:1px solid #f4f4f4}
</style>


<script>
document.addEventListener('DOMContentLoaded', function () {
  var heads = Array.prototype.slice.call(document.querySelectorAll('h2.bibliography'));
  if (!heads.length) return;
  var idx = document.getElementById('pubindex'), made = [];
  heads.forEach(function (h, k) {
    var list = h.nextElementSibling;
    while (list && list.tagName !== 'OL' && list.tagName !== 'UL') list = list.nextElementSibling;
    if (!list) return;
    var n = list.querySelectorAll(':scope > li').length;
    var d = document.createElement('details');
    d.className = 'pubcat';
    d.id = 'cat-' + k;
    var sm = document.createElement('summary');
    sm.innerHTML = h.textContent + '<span class="n">' + n + '</span>';
    h.parentNode.insertBefore(d, h);
    d.appendChild(sm); d.appendChild(list); h.remove();
    made.push({el: d, name: h.textContent, n: n});
  });
  made.forEach(function (m) {
    var c = document.createElement('span');
    c.className = 'chip';
    c.innerHTML = m.name + '<b>' + m.n + '</b>';
    c.onclick = function () {
      m.el.open = true;
      m.el.scrollIntoView({behavior: 'smooth', block: 'start'});
    };
    idx.appendChild(c);
  });
  var all = document.createElement('span');
  all.className = 'chip allbtn';
  all.textContent = 'expand all';
  all.onclick = function () {
    var open = all.textContent === 'expand all';
    made.forEach(function (m) { m.el.open = open; });
    all.textContent = open ? 'collapse all' : 'expand all';
  };
  idx.appendChild(all);
});
</script>

<hr>

### Copyright Notice

The documents listed here are available for downloading and have been provided as a means to ensure timely dissemination of scholarly and technical work on a noncommercial basis. Copyright and all rights therein are maintained by the authors or by other copyright holders, notwithstanding that they have offered their works here electronically. It is understood that all persons copying this information will adhere to the terms and constraints invoked by each author's copyright. These works may not be re-posted without the explicit permission of the copyright holder.
