# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0018_auto_20151103_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f103',
            name='Occupation_F',
            field=birth_registration.fields.ExtraOccupationField(max_length=100, null=True, verbose_name='Occupation (optional description)', blank=True),
        ),
        migrations.AlterField(
            model_name='f103',
            name='Occupation_M',
            field=birth_registration.fields.ExtraOccupationField(max_length=100, null=True, verbose_name='Occupation (optional description)', blank=True),
        ),
        migrations.AlterField(
            model_name='f203',
            name='Occupation',
            field=birth_registration.fields.ExtraOccupationField(max_length=100, verbose_name='Occupation (optional description)', blank=True),
        ),
    ]
