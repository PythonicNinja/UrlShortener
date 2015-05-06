# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlslug',
            name='is_used',
            field=models.BooleanField(default=False, help_text='checked if was used as slug', db_index=True, verbose_name='Used'),
        ),
    ]
