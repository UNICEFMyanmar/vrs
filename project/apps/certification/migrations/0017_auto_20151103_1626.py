# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0016_auto_20150922_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='f103',
            name='Occupation',
            field=birth_registration.fields.ExtraOccupationField(help_text='Optional description', max_length=100, verbose_name='Occupation (extra)', blank=True),
        ),
        migrations.AddField(
            model_name='f203',
            name='Occupation',
            field=birth_registration.fields.ExtraOccupationField(help_text='Optional description', max_length=100, verbose_name='Occupation (extra)', blank=True),
        ),
    ]
