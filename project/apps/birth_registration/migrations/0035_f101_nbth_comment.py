# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0034_auto_20151103_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='f101',
            name='NBTH_comment',
            field=birth_registration.fields.Char300Field(max_length=300, null=True, verbose_name='Optional comment', blank=True),
        ),
    ]
