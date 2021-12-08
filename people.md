---
title: People
permalink: /research/people/
---

{% assign people_sorted = site.people | sort: 'joined' %}
{% assign role_array = "pi|postdoc|gradstudent|researchstaff|visiting|others|alumni" | split: "|" %}

{% for role in role_array %}

{% assign people_in_role = people_sorted | where: 'position', role %}

<!-- Skip section if there's nobody -->
{% if people_in_role.size == 0 %}
  {% continue %}
{% endif %}

<div class="pos_header">
{% if role == 'postdoc' %}
<h3>Postdoctoral Fellows</h3>
 {% elsif role == 'pi' %}
<h3>Principal Investigator</h3>
 {% elsif role == 'gradstudent' %}
<h3>Graduate Students</h3>
 {% elsif role == 'researchstaff' %}
<h3>Research Staff</h3>
 {% elsif role == 'visiting' %}
<h3>Visiting Scholars</h3>
 {% elsif role == 'others' %}
<h3>Honorary Members</h3>
 {% elsif role == 'alumni' %}
<h3>Alumni</h3>
{% endif %}
</div>

{% if role != 'alumni' %}
<div class="content list people">
  {% for profile in people_sorted %}
    {% if profile.position contains role %}
      <div class="list-item-people">
        <p class="list-post-title">
          {% if profile.avatar %}
            <a href="{{ site.baseurl }}{{ profile.url }}"><img class="profile-thumbnail" src="{{site.baseurl}}/images/people/{{profile.avatar}}"></a>
          {% else %}
            <a href="{{ site.baseurl }}{{ profile.url }}"><img class="profile-thumbnail" src="http://evansheline.com/wp-content/uploads/2011/02/facebook-Storm-Trooper.jpg"></a>
          {% endif %}
          <a class="name" href="{{ site.baseurl }}{{ profile.url }}">{{ profile.name }}</a>
        </p>
      </div>    
    {% endif %}
  {% endfor %}
</div>
<hr>

{% else %}

<br>

| Who are they | What did they do |When were they here | Where they went |
| :------------- |:------------- |:------------------| :-----------|
| Shammya Saha | Power Systems | PhD (2016-2021) | Joined Electric Power Research Institute (EPRI) as Scientist II in July 2021 |
| [Raksha Ramakrishna](/people/raksha_ramakrishna) | Signal Processing, Power Systems | PhD (2015-2020) | Joined KTH Royal Institute of Technology as Postdoctoral Researcher in September 2020 |
| Kári Hreinsson | Power Systems | PhD (2015-2020) | Joined Veitur Electric Distribution, Iceland, as Research and Development Lead in August 2020 |
| Teklamariam Tesfay | Power Systems, Cybersecurity | Postdoc (2017-2018) | Joined NASA Jet Propulsion Laboratory as Cybersecurity Engineer |
| Eran Schweitzer | Power Systems | PhD (2015-2018) | Joined STEAG Energy Services GmbH, Essen, Germany, as Project Engineer |
| Mahdi Jamei | Power Systems | PhD (2014-2018) | Joined Invenia Labs, Cambridge, UK, as Researcher in September 2018 |
| Hoi-To Wai | Optimization, Signal Processing, Network Science | PhD (2013-2017) | Joined Chinese University of Hong Kong as Assistant Professor |
| Lorenzo Ferrari | Communications | PhD (2014-2017) | Joined Qualcomm as a Senior Engineer |
| Reinhard Gentz | Communications | PhD (2013-2017) | Joined Data Science and Technology Department, in the Computational Research division at Lawrence Berkeley National Laboratories, USA as a Computer Software Engineer |
| Xiaoxiao Wu | Signal Processing, Optimization | Postdoc (2014-2015) | Joined Shenzhen University, China as Assistant Professor in 2017 |
| Masood Parvania | Power Systems | Postdoc (2014-2015) | Joined University of Utah as Assistant Professor in 2015 |
| Irene Spanou |  | M.S. (2012-2014) | Graduated in March 2014 |
| Mahnoosh Alizadeh | Power Systems | PhD (2009-2014) | Joined the group of Prof. Andrea Goldsmith as a Postdoctoral Scholar in Stanford |
| Saeed Bagheri | Communications | PhD (2009-2014) | Joined Qualcomm |
| Georgia Koustandria |  | M.S. (2012-2014) | PhD student at the University of Rome La Sapienza |
| Xiao Li | Signal Processing, Power Systems | PhD (2009-2013) | Joined the group of Prof. Kannan Ramanchandran as Post-Doctoral Scholar at UC Berkeley |
| Lin Li | Signal Processing | PhD (2008-2013) | Joined ARL |
| Andrea Rueetschi | Communications | PhD (2007-2013) | Joined ABB |
| Tsung-Hui Cheng | Signal Processing, Optimization | Postdoc (2011-2012) | Joined National Taiwan University of Science and Technology as Assistant Professor in 2012 |
| Zhifang Wang | Power Systems | Postdoc (2008-2012) | Joined VSU as Assistant Professor in 2012 |
| Matthew Sharp | Communications | PhD (2005-2011) | Joined Johns Hopkins University Applied Physics Laboratory |
| Ramy Tannious | Information Theory | Postdoc (2008-2010) | Joined Aviat Networks in 2011 |
| Roberto Pagliari | Network science | PhD (2006-2010) | Currently with Applied Communication Sciences |
| Ercan Yildiz | Signal Processing | PhD (2005-2010) | Joined Accenture Technology Labs, now with Google |
| Shrut Kirti | Communications | PhD (2005-2010) | Joined Ropes & Gray LLP as Technical Advisor |
| Stephen Lim |  | M.S. (2008-2010) | Graduated in June 2010 |
| David Perkins, Jalal Elidrissi, Chaoyi Ye | | Undergrad Research (2009) | | 
| Tuncer Can Aysal | Signal Processing | Postdoc (2007-2008) | Joined Weston Capital Management in 2008 |
| Eric Alexander Jarva | | Undergrad Research (2007) | | 
| Jeff Woodworth | | Undergrad Research (2006) | | 
| Zheshen Zhuang |  | M.Eng. | Graduated in May 2006 |
| Dennis Yueping Leung |  | M.Eng. | Graduated in May 2006 |
| Azadeh Vosoughi | Communications | PhD (2001-2006) | Joined the faculty at the University of Rochester in September 2006. She is currently Associate Professor at the University of Central Florida, since 2012 |
| Birsen Sirkeci | Communications | PhD (2002-2006) | Joined UC Berkley as a Postdoctoral Researcher in 2007. She joined the faculty at San Jose State University in September 2007 |
| Yao-Win-Hong | Communications | PhD (2001-2005) | Joined the faculty at National Tsing Hua University – NTHU – in Taiwan in 2005 where he is currently Full Professor |
| Bibo Xu | | Undergrad Research (2005) | | 
| Jade Lin |  | M.Eng. | Graduated in May 2005 |
| Lih Feng Cheow, Abhijeet Agarwal | | Undergrad Research (2004) | | 
| Aman Chawla | | Undergrad Research (2004) | | 
| Atul Salhotra |  | M.S. (2001-2004) | Graduated in January 2004 |
| Avik Sur |  | M.Eng. | Graduated in December 2003 |
| Alan Tsui |  | M.Eng. | Graduated in December 2003 |
| Laura Hotca |  | M.Eng. | Graduated in August 2003 |
| Dalia Burgos |  | M.Eng. | Graduated in August 2003 |
| Obianuju Ndili |  | M.S. (2001-2003) | Graduated in August 2003 |
| Lih Feng Cheow, Chihiro Fukami, Aman Chawla | | Undergrad Research (2003) | | 
| Marvin Chan, Eng Hwa Leonard Lim, Zhi Wei Kam | | Undergrad Research (2003) | | 
| Luke Hejnar |  | M.Eng. | Graduated in May 2003 |
| Santiago Castillo |  | M.Eng. | Graduated in May 2003 |
| Linda Pan, Olasubomi Oluwatobi Awe | | Undergrad Research (2002) | | 
| Luke Hejnar and Yulin Wang| | Undergrad Research (2002) | |
| Francisco Rafael Bastistas |  | M.Eng. | Graduated in May 2002 |
| Rahul Kopikar |  | M.Eng. | Graduated in May 2002 |
| Gaelle Isabelle Protat |  | M.Eng. | Graduated in May 2002 |
| Unal Sakoglu |  | M.S. (2000-2001) | Graduated May 2001 |

{% endif %}
{% endfor %}
