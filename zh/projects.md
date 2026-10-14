---
layout: default
title: 项目
permalink: /zh/projects/
lang: zh-CN
translation_key: projects
---

# 项目 {#projects}

部分项目，涵盖面向心理健康与学习的人机协作、立足文化语境的叙事与游戏智能，以及数字文化遗产。

{% assign other_projects = site.data.projects | where_exp: "project", "project.category != 'games'" %}
{% include project-list.html projects=other_projects %}
