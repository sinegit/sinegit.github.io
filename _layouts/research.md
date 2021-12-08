---
layout: default
---
<div class="container content page">
  <h3 class="page-title">{{ page.name }}</h3>
  {% if page.image %}
    <img width="300" src="{{site.baseurl}}/images/people/{{page.image}}" data-action="zoom">
  {% else %}
    <img width="300" src="https://evansheline.com/wp-content/uploads/2011/02/facebook-Storm-Trooper.jpg"  data-action="zoom">
  {% endif %}
  <p> {{page.description}} <p>
  {% if page.projects %}
 Funded Projects
 <ul>
 {% for project in page.projects %}
 <li><a href="{{project.link}}">{{project.title}}</a></li>
 {% endfor %}
 </ul>
 {% endif %}
  <!-- {{ content }} -->
</div>
