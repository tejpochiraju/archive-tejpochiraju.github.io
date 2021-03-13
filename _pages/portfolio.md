---
layout: default
permalink: /portfolio/
---

<a href="/filter/">Filter Projects</a>
<br/>
<br/>

<div class="columns">
  {% assign display_tags = "" %}
  {% assign arena = "Startup" %}
  {% include column.html %}
  {% assign arena = "Corporate" %}
  {% include column.html %}
  {% assign arena = "Academia" %}
  {% include column.html %}
</div>