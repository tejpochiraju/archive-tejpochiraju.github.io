---
layout: default
permalink: /contact/
published: false
---


<ul>
    {% if site.email != "" %}
        <li>
            Write to me at <a href="mailto:{{ site.email }}" target="_blank">{{ site.email }}</a>
        </li>
    {% endif %}

    {% if site.linkedin != "" %}
        <li>
            Connect with me on <a href="https://www.linkedin.com/in/{{ site.linkedin }}" target="_blank">LinkedIn</a>
        </li>
    {% endif %}

    {% if site.twitter != "" %}
        <li>
            Follow me on <a href="https://twitter.com/{{ site.twitter }}" target="_blank">Twitter</a>
        </li>
    {% endif %}

    {% if site.github != "" %}
        <li>
            Explore the code for this site and other open source projects on <a href="https://github.com/{{ site.github }}" target="_blank">Github</a>
        </li>
    {% endif %}
</ul>