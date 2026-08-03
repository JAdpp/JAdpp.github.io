---
layout: default
title: Home
---

<section class="hero">
  <h1>Hi, I'm Yangming Zhang.</h1>
  <div class="hero__content">
    <p class="lead">
      I'm a Ph.D. student in the School of Information Management at Wuhan University, advised by Assoc. Prof. Liang Zhao and Prof. Jie Xu, and a student researcher at the <a href="https://iclch.whu.edu.cn/">Intelligent Computing Laboratory for Cultural Heritage (ICLCH)</a>. I work on Human-AI collaboration, culturally grounded multimodal LLM agents, and AI systems for wellbeing, education, and digital cultural heritage.
    </p>
    <p>
      My current research asks how AI systems can support culturally situated human needs: from classical Chinese poetry as emotional support, to multi-agent educational systems, to generative curation for cultural heritage. I build interactive prototypes and evaluate them through user studies and mixed methods.
    </p>
    <p>
      Previously, I received an M.Sc. in Digital Humanities from University College London (UCL) and a B.Sc. from Wuhan University.
    </p>
  </div>
  <aside class="hero__aside">
    <figure class="hero__portrait">
      <img src="{{ '/assets/img/yangming-zhang.jpg' | relative_url }}" alt="Portrait of Yangming Zhang">
    </figure>
    <div class="text-links hero__links" aria-label="Profile links">
      <a href="{{ site.links.scholar }}">Google Scholar</a>
      <a href="{{ site.links.github }}">GitHub</a>
      <a href="{{ site.links.cv | relative_url }}">CV</a>
      <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a>
    </div>
  </aside>
</section>

<section class="section-grid">
  <div>
    <h2>Research Interests</h2>
    <ul class="interest-list">
      <li>Human-AI collaboration and human-centered evaluation</li>
      <li>Culturally grounded AI agents and multimodal LLM systems</li>
      <li>AI for Wellbeing, education, and creative support</li>
      <li>Digital cultural heritage and computational humanities</li>
    </ul>
  </div>
  <div>
    <h2>Latest News</h2>
    <div class="news-list">
      {% for item in site.data.news limit:4 %}
        <p><span>{{ item.date }}</span> <a href="{{ item.link }}">{{ item.text }}</a></p>
      {% endfor %}
    </div>
  </div>
</section>

<section>
  <div class="section-heading">
    <h2>Featured Publications</h2>
    <a href="{{ '/publications/' | relative_url }}">All publications</a>
  </div>
  {% assign featured_publications = site.data.publications | where: "featured", true %}
  {% include publication-list.html publications=featured_publications %}
</section>

<section>
  <div class="section-heading">
    <h2>Selected Projects</h2>
    <a href="{{ '/projects/' | relative_url }}">All projects</a>
  </div>
  {% assign featured_projects = site.data.projects | where: "featured", true %}
  {% include project-list.html projects=featured_projects %}
</section>
