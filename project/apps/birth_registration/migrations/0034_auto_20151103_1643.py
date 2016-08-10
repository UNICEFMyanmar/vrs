# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0033_auto_20151103_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f101',
            name='Occupation_F',
            field=birth_registration.fields.ExtraOccupationField(max_length=100, verbose_name='Occupation (optional description)', blank=True),
        ),
        migrations.AlterField(
            model_name='f101',
            name='Occupation_M',
            field=birth_registration.fields.ExtraOccupationField(max_length=100, verbose_name='Occupation (optional description)', blank=True),
        ),
        migrations.AlterField(
            model_name='f201',
            name='Occupation',
            field=birth_registration.fields.ExtraOccupationField(max_length=100, verbose_name='Occupation (optional description)', blank=True),
        ),
    ]
