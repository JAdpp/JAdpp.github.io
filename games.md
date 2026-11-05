---
layout: default
title: Games & Interaction
permalink: /games/
lang: en
translation_key: games
---

# Games & Interaction {#games}

Silent previews combine title cards with project highlights. Recorded builds may be newer than the linked playable prototypes.

{% assign games = site.data.projects | where: "category", "games" %}
{% include project-list.html projects=games %}
