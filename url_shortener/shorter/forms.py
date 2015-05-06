# -*- coding: utf-8 -*-
# CREATED ON DATE: 06.05.15
from __future__ import absolute_import, unicode_literals

__author__ = 'mail@pythonic.ninija'


from django import forms


from .models import Url


class UrlForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = ("url", )
