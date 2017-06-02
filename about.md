---
layout: page
title: 关于
header: 关于
group: navigation
weight: 1
---
{% include JB/setup %}

Welcome to Edge Fund 
Apply [Market Timing](http://en.wikipedia.org/wiki/Market_timing) as an engineering..  

<h2> Latest </h2>
<ul class="posts">
  {% for post in site.posts limit:5 %}
    <li><span>{{ post.date | date_to_utc | date: '%Y-%m-%d' }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

<!-- Styles -->
<link rel="stylesheet" media="all" href="./image/site.min.css" type="text/css">
<!-- Modernizr -->
<script src="./image/modernizr.min.js"></script>
