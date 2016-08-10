# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0035_f101_nbth_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='f201',
            name='NRC',
            field=birth_registration.fields.Char100Field(max_length=100, null=True, verbose_name='NRC', blank=True),
        ),
    ]
