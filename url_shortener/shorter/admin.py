# -*- coding: utf-8 -*-
# CREATED ON DATE: 06.05.15
__author__ = 'mail@pythonic.ninija'

from django.contrib import admin

from .models import UrlSlug, Url

admin.site.register([
    Url,
    UrlSlug
])
