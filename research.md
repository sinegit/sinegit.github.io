---
title: Research
permalink: /research/
# layout: default
---

### Research Areas

Directed by Anna Scaglione, the Signal, Information, Networks and Energy (SINE) laboratory (formerly known as the CRISP Lab) was established in Cornell University in 2001. It was hosted by Cornell University (2001-2008), University of California, Davis (2008-2014), Arizona State University (2014-2021), prior to moving back to Cornell University. The SINE Lab’s research focuses on the intersection of signal processing, network science and energy systems.

- Distributed Optimization:
    - [NeTS: Small: LayBack: Layered SDN-Based Backhaul Architecture and Optimization Framework for Small Cells and Beyond](https://faculty.engineering.asu.edu/mre/research/layback/)
- Reliable Energy Delivery Systems:
    - [Provable Anonymization of Grid Data for Cyberattack Detection](https://dst.lbl.gov/security/project/ceds-privacy/)
    - [Supervisory Parameter Adjustment for Distribution Energy Storage (SPADES)](https://dst.lbl.gov/security/project/ceds-spades/)
- Industrial Internet of Things (IIoT):
    - [Evaluation of the LwM2M Protocol and 5G Networks Performance for wide-area Industrial Internet of Thing](/projects/xylem)
- Grid Graph Signal Processing
    - [Neptune 2.0: Situation Awareness and Smart Reconfiguration of Ad-hoc Military Electric Grids Using a Digital-twin](/projects/neptune2_0)


{% comment %} 
<!-- {% include carousel.html height="50" unit="%" duration="7" %} -->
 <hr style="clear:both;">
{% for research in site.research %}
- **{{ research.name }}**
 {% if research.image %}
 <img src= "{{site.baseurl}}/images/research/{{research.image}}" align="left" vspace="400" hspace="400" style="padding: 10px 10px 10px 10px">
 {% else %}
 <img src= "http://evansheline.com/wp-content/uploads/2011/02/facebook-Storm-Trooper.jpg" vspace="40" hspace="40" style="padding: 10px 10px 10px 10px">
 {% endif %}
 {% if research.description %}{{ research.description }}{% endif %}
 {% if research.projects %}
 Funded Projects
 : {% for project in research.projects %}
 - [{{project.title}}]({{project.link}})
 {% endfor %}
 {% endif %}

 {% capture bib_count %}{% bibliography_count -q @*[research={{ research.title }}] %}{% endcapture %}
 {% assign bib_count = bib_count | plus: 0 %}

 {% if bib_count > 0 %}
 <strong>Recent Publications</strong>: 
 {% bibliography --group_by none --max 3 -q @*[research= {{ research.title }}] --sort_by year --order descending %}
 {% endif %}
 <hr style="clear:both;">
 {% endfor %}
 {% endcomment %}