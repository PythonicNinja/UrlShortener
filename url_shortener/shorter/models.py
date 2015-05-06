# -*- coding: utf-8 -*-
# CREATED ON DATE: 06.05.15
__author__ = 'mail@pythonic.ninija'

import re
from operator import __or__ as OR

from django.db import models
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class Url(TimeStampedModel):
    url = models.URLField(verbose_name=_('Url'), help_text=_('used for shortening'), unique=True, db_index=True)
    slug = models.ForeignKey('shorter.UrlSlug', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('shorter:url_detail', kwargs={'slug': self.slug.slug})

    @classmethod
    def split_url_into_words(cls, url):
        '''
        >>> Url.split_url_into_words('http://techcrunch.com/2012/12/28/pinterest-lawsuit/')
        ['http', 'techcrunch', 'com', '2012', '12', '28', 'pinterest', 'lawsuit']
        '''
        return re.findall(r"[\w']+", url)

    def asign_slug(self):
        available_slugs = UrlSlug.objects.filter(is_used=False)
        
        if not available_slugs.exists():
            raise EnvironmentError('Please import some url slugs by command \n ./manage.py import_words -f filename.txt')

        words_in_url = Url.split_url_into_words(self.url)
        query_words = [Q(slug=word) for word in words_in_url]

        slugs_for_word = available_slugs.filter(reduce(OR, query_words))

        if slugs_for_word.exists():
            self.slug = slugs_for_word.first()
        else:
            self.slug = available_slugs.first()

        self.slug.is_used = True
        self.slug.save()

    def save(self, *args, **kwargs):
        self.asign_slug()
        super(Url, self).save(*args, **kwargs)


class UrlSlug(TimeStampedModel):
    slug = models.SlugField(verbose_name=_('Slug field'), help_text=_('slug to generate url'))
    is_used = models.BooleanField(verbose_name=_('Used'), help_text=_('checked if was used as slug'),
                                  default=False, db_index=True)
    word = models.CharField(verbose_name=_('Word'), help_text=_('original word'), max_length=255)
