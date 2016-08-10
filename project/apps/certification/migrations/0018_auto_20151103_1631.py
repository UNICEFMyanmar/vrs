# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0017_auto_20151103_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='f103',
            name='Occupation',
        ),
        migrations.AddField(
            model_name='f103',
            name='Occupation_F',
            field=birth_registration.fields.ExtraOccupationField(help_text='Optional description', max_length=100, null=True, verbose_name='Occupation (extra)', blank=True),
        ),
        migrations.AddField(
            model_name='f103',
            name='Occupation_M',
            field=birth_registration.fields.ExtraOccupationField(help_text='Optional description', max_length=100, null=True, verbose_name='Occupation (extra)', blank=True),
        ),
    ]
