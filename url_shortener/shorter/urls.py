# -*- coding: utf-8 -*-
# CREATED ON DATE: 06.05.15
from __future__ import absolute_import, unicode_literals

__author__ = 'mail@pythonic.ninija'

from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(regex=r'^$', view=views.UrlInput.as_view(), name='url_input'),
    url(regex=r'^(?P<slug>[\w.@+-]+)/detail/$', view=views.UrlDetail.as_view(), name='url_detail'),
    url(regex=r'^(?P<slug>[\w.@+-]+)/$', view=views.UrlRedirect.as_view(), name='url_redirect'),
)
