---
title: Photos
permalink: /photos/
description: "Photos"
---

# SINE Lab photos

<ul>
  {% comment %}
    Get all "photo_set" pages and display a list with links to them.
  {% endcomment %}
  {% assign photo_pages = site.photos | where: "layout", "photo_set" | sort: 'date' %}
  {% for photo_page in photo_pages %}
    <li>
      <a href="{{ photo_page.url | prepend: site.url/photos }}">{{ photo_page.title }}</a>
    </li>
  {% endfor %}
</ul>