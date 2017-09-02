---
layout: default
permalink: /filter/
---

<div>
    <h1><strong>Filter projects by clicking on any of the categories below.</strong></h1>
    <br/>
    <div class="columns">
    {% assign navlist = site.data.navigation.nav | sort: 'title' %}
    {% for item in navlist %}
        <div class="column">
            <h3><strong>{{ item.title }}</strong></h3>
            <ul>
            {% assign entrylist = item.items | sort: 'page' %}
            {% for entry in entrylist %}
              <li><a href="{{ entry.url }}">{{ entry.page }}</a></li>
            {% endfor %}
            </ul>
        </div>
    {% endfor %}
    </div>
</div>