---
layout: default
title: Projects
permalink: /projects/
lang: en
translation_key: projects
---

# Projects {#projects}

Selected projects in Human-AI collaboration for mental wellbeing and learning, culturally grounded narrative and game intelligence, and digital cultural heritage.

{% assign other_projects = site.data.projects | where_exp: "project", "project.category != 'games'" %}
{% include project-list.html projects=other_projects %}
