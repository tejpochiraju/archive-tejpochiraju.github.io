---
layout: default
permalink: /clients/
published: false
---

<div>
{% for image in site.static_files %}
    {% if image.path contains 'assets/images/clients' %}
        <figure class="image is-128x128">
            <img src="{{ site.baseurl }}{{ image.path }}" alt="image" />
        </figure>
    {% endif %}
{% endfor %}
</div>