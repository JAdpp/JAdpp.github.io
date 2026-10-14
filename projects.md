---
layout: default
title: Projects
permalink: /projects/
---

# Projects

Selected projects in Human-AI collaboration for mental wellbeing and learning, culturally grounded narrative and game intelligence, and digital cultural heritage.

{% assign other_projects = site.data.projects | where_exp: "project", "project.category != 'games'" %}
{% include project-list.html projects=other_projects %}

<section id="games" aria-labelledby="games-heading">
  <div class="section-heading">
    <h2 id="games-heading">Games &amp; Interactive Experiences</h2>
  </div>
  {% assign games = site.data.projects | where: "category", "games" %}
  {% include project-list.html projects=games %}
</section>
