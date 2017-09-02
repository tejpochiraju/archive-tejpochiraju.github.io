---
layout: default
permalink: /
---

<div class="tile is-ancestor">
  <div class="tile is-vertical is-4">
    <div class="tile">
      <div class="tile is-parent is-vertical">
        <figure class="image is-256x256">
            <img src="{{ site.photo }}" alt="Image">
        </figure>
      </div>
    </div>
  </div>
  <div class="tile is-parent">
    <!-- <article class="tile is-child"> -->
      <div class="content">
        <div class="content">
            <p>
                {{ site.bio }}
            </p>
            I am affiliated with:<br/>
            {% for affiliation in site.affiliations %}
                <a href="affiliation.url">{{ affiliation.title }}</a> - {{ affiliation.bio }}<br/>
            {% endfor %}
        </div>
      </div>
    <!-- </article> -->
  </div>
</div>
