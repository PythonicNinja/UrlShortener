# -*- coding: utf-8 -*-
# CREATED ON DATE: 06.05.15
from __future__ import absolute_import, unicode_literals

__author__ = 'mail@pythonic.ninija'

from django.http import HttpResponseRedirect
from django.views.generic import RedirectView, CreateView, DetailView


from .forms import UrlForm
from .models import Url


class UrlInput(CreateView):
    form_class = UrlForm
    template_name = 'shorter/url_input.html'

    def form_invalid(self, form):
        url = form['url'].value()
        if url:
            self.object, created = Url.objects.get_or_create(**{'url': url})
            return HttpResponseRedirect(self.get_success_url())
        else:
            super(UrlInput, self).form_invalid(form)


class UrlDetail(DetailView):
    model = Url
    slug_field = 'slug__slug'
    template_name = 'shorter/url_details.html'
    context_object_name = 'url'


class UrlRedirect(DetailView):
    model = Url
    slug_field = 'slug__slug'

    def get(self, *args, **kwargs):
        object = self.get_object()
        return HttpResponseRedirect(object.url)
