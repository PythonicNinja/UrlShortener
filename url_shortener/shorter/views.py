# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView, CreateView, DetailView


from .forms import UrlForm
from .models import Url


class UrlInput(CreateView):
    form_class = UrlForm
    template_name = 'shorter/url_input.html'

    def form_invalid(self, form):
        self.object, created = Url.objects.get_or_create(**{'url': form['url'].value()})
        return HttpResponseRedirect(self.get_success_url())


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
