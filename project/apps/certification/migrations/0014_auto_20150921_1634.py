# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0013_auto_20150921_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f203',
            name='SEX',
            field=birth_registration.fields.SEXField(verbose_name='Sex', choices=[(1, '01 - Male'), (2, '02 - Female'), (9, '09 - Not stated')]),
        ),
    ]
