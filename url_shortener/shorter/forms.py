# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms


from .models import Url


class UrlForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = ("url", )
