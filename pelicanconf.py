#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'SIRA'

SITENAME = u'Society of Information Risk Analysts'
# SITEURL = 'http://dds.ec/sirastg'
# SITEURL = 'http://localhost:8000/stg'
SITEURL = 'https://www.societyinforisk.org/stg'
SITELOGO = 'images/sira-logo.png'
SITELOGO_SIZE = '40'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

READERS = {'html': None}

SUMMARY_MAX_LENGTH = 250

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'authors'))
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc', 'footnotes']

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True

THEME = "pelican-themes/tuxlite_tbs"
PLUGIN_PATH = "plugins"
PATH = "../blog/content/"

PAGE_URL = u'pages/{slug}.html'
PAGE_SAVE_AS = u'pages/{slug}.html'

TAG_URL = u'tag/{slug}.html'
TAG_SAVE_AS = u'tag/{slug}.html'
TAG_FEED_ATOM = 'feeds/tag/%s.atom.xml'

AUTHOR_URL = u'author/{slug}.html'
AUTHOR_SAVE_AS = u'author/{slug}.html'

AUTHORS_URL = u'authors.html'
AUTHORS_SAVE_AS = u'authors.html'

CATEGORY_FEED_ATOM = 'feeds/category/%s.atom.xml'
CATEGORY_URL = u'category/{slug}.html'

CATEGORY_SAVE_AS = u'category/{slug}.html'
CATEGORIES_SAVE_AS = 'categories.html'

CUSTOM_CSS = 'static/custom.css'
# Tell Pelican to add 'extra/custom.css' to the output dir
STATIC_PATHS = ['images', 'extra/custom.css']
#OUTPUT_PATH = '../output'
OUTPUT_PATH = '/var/www/societyinforisk/stg'

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'}
}

MENUBRAND = [("SIRA - Society of Information Risk Analysts", "http://societyinforisk.org"),]
# SOCIAL_SIDEBAR_TOP = (
#       ('Google+', 'https://plus.google.com/', '<i class="icon-google-plus-sign"></i>'),
#       ('Twitter', 'https://twitter.com/societyinforisk', '<i class="icon-twitter-sign"></i>'),
#       )
#PLUGINS = ['extract_toc', 'tipue_search']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives'))
TYPOGRIFY = True

DISQUS_SITENAME = u'societyinforisk'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
TRANSLATION_FEED_ATOM = None
FEED_MAX_ITEMS = 20

TWITTER_USERNAME = "societyinforisk"

GITHUB_URL = ''
TWITTER_URL = 'http://twiter.com/societyinforisk'
FACEBOOK_URL = ''
GOOGLEPLUS_URL = ''
GOOGLE_ANALYTICS_ID = ''
GOOGLE_ANALYTICS_SITENAME = ''
# Blogroll


LINKS =  (('Open Group FAIR Certification', 'http://www.opengroup.org/certifications/openfair'),
          ('Guide to Developing a Cyber Security and Risk Mitigation Plan', 'https://www.smartgrid.gov/sites/default/files/doc/files/CyberSecurityGuideforanElectricCooperativeV11-2%5B1%5D.pdf'),
          ('NIST Home > Cybersecurity Framework', 'http://www.nist.gov/cyberframework/'),)

# Social widget
SOCIAL = (('SocietyInfoRisk', 'http://twitter.com/societyinforisk'), )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
