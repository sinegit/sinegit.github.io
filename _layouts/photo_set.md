---
layout: default
---

{% assign num = page.photos.size %}
<div class="container content page">
  <h3 class="page-title">{{ page.title }}</h3>
  {% for i in (1..num) %}
    <img src="{{ site.url }}/images/photos/{{ page.photos.set }}-{{ i }}.jpg" alt="Photo {{ i }} from {{ page.photos.set | capitalize }}"  data-action="zoom">
  {% endfor %}

<div>
  <a href="{{ site.url }}/photos/">View All Photo Sets</a>
</div>
</div>
