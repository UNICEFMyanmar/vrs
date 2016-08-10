# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0032_auto_20151103_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='f101',
            name='Occupation',
        ),
        migrations.AddField(
            model_name='f101',
            name='Occupation_F',
            field=birth_registration.fields.ExtraOccupationField(help_text='Optional description', max_length=100, verbose_name='Occupation (extra)', blank=True),
        ),
        migrations.AddField(
            model_name='f101',
            name='Occupation_M',
            field=birth_registration.fields.ExtraOccupationField(help_text='Optional description', max_length=100, verbose_name='Occupation (extra)', blank=True),
        ),
    ]
