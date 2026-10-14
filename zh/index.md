---
layout: default
title: 首页
permalink: /zh/
lang: zh-CN
translation_key: home
---

<section class="hero" id="about">
  <h1>你好，我是张扬明。</h1>
  <div class="hero__content">
    <p class="lead">
      我是武汉大学信息管理学院的博士生，师从赵靓副教授和许洁教授，同时是<a href="https://iclch.whu.edu.cn/">文化遗产智能计算实验室（ICLCH）</a>的学生研究员。我的研究关注人机协作、立足文化语境的多模态大语言模型智能体，以及面向心理健康、教育和数字文化遗产的人工智能系统。
    </p>
    <p>
      我目前关注人工智能系统如何回应具体文化语境中的人的需求：从借助中国古典诗词提供情感支持，到多智能体教育系统、文化遗产的生成式策展，以及 AI 原生游戏与交互叙事。我构建交互原型，并通过用户研究和混合方法开展评估。
    </p>
    <p>
      此前，我获得了伦敦大学学院（UCL）的数字人文理学硕士学位，以及武汉大学的管理学学士学位。研究之外，我喜欢以动漫和游戏为灵感进行同人创作。
    </p>
  </div>
  <aside class="hero__aside">
    <figure class="hero__portrait">
      <img src="{{ '/assets/img/yangming-zhang-candid-640.webp' | relative_url }}" srcset="{{ '/assets/img/yangming-zhang-candid-640.webp' | relative_url }} 640w, {{ '/assets/img/yangming-zhang-candid-960.webp' | relative_url }} 960w" sizes="(max-width: 780px) 261px, 316px" alt="张扬明的照片" width="960" height="1282" fetchpriority="high" decoding="async">
    </figure>
    <div class="text-links hero__links" aria-label="个人资料链接">
      <a href="{{ site.links.scholar }}">Google Scholar</a>
      <a href="{{ site.links.github }}">GitHub</a>
      <a href="{{ site.links.cv | relative_url }}">简历（英文 PDF）</a>
      <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a>
    </div>
  </aside>
</section>

<section class="section-grid">
  <div>
    <h2 id="research-interests">研究方向</h2>
    <ul class="interest-list">
      <li>面向心理健康与学习的人机协作</li>
      <li>立足文化语境的多模态智能体、创意系统与游戏智能</li>
      <li>数字文化遗产与计算人文</li>
    </ul>
  </div>
  <div>
    <h2 id="latest-news">最新动态</h2>
    <div class="news-list">
      {% for item in site.data.news limit:4 %}
        {% assign news_text = item.text_zh | default: item.text %}
        <p><span>{{ item.date_zh | default: item.date }}</span> {% if item.link %}<a href="{{ item.link }}">{{ news_text }}</a>{% else %}{{ news_text }}{% endif %}</p>
      {% endfor %}
    </div>
  </div>
</section>

<section>
  <div class="section-heading">
    <h2 id="featured-publications">精选论文</h2>
    <a href="{{ '/zh/publications/' | relative_url }}">全部论文</a>
  </div>
  {% assign featured_publications = site.data.publications | where: "featured", true %}
  {% include publication-list.html publications=featured_publications %}
</section>

<section>
  <div class="section-heading">
    <h2 id="selected-projects">精选项目</h2>
    <a href="{{ '/zh/projects/' | relative_url }}">全部项目</a>
  </div>
  {% assign featured_projects = site.data.projects | where: "featured", true | where_exp: "project", "project.category != 'games'" %}
  {% include project-list.html projects=featured_projects %}
</section>
