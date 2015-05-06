# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('url', models.URLField(help_text='used for shortening', verbose_name='Url')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UrlSlug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('slug', models.SlugField(help_text='slug to generate url', verbose_name='Slug field')),
                ('is_used', models.BooleanField(default=False, help_text='checked if was used as slug', verbose_name='Used')),
                ('word', models.CharField(help_text='original word', max_length=255, verbose_name='Word')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='url',
            name='slug',
            field=models.ForeignKey(blank=True, to='shorter.UrlSlug', null=True),
        ),
    ]
