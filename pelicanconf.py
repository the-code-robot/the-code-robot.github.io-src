#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Robin Abbi'
SITENAME = u'CodeRobot'
SITEURL = u'http://coderobot.downley.net'

THEME = u'/home/robin/Projects/bulrush/'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'assets']


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'weekly'
    }
}

JINJA_ENVIRONMENT = {
   'extensions': ['webassets.ext.jinja2.AssetsExtension',
                  'jinja2.ext.with_'],
}

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
   ('Semantic Web', 'https://www.w3.org/standards/semanticweb/'),
   ('Pieter Hintjens', 'http://hintjens.com/'),
   ('Python.org', 'http://python.org/'),
   ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/_coderobot'),
    ('linkedin', 'https://www.linkedin.com/in/robinabbi/'),
    ('stackoverflow', 'http://stackoverflow.com/users/4999639/coderobot'),
)

DEFAULT_PAGINATION = False
GOOGLE_ANALYTICS = "UA-92650351-1"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
