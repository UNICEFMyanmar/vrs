# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0005_auto_20150910_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='f103',
            name='NR_AREA',
            field=birth_registration.fields.AreaField(default=1, help_text='Urban/Rural', verbose_name='Area', choices=[(1, '01 - Urban'), (2, '02 - Rural')]),
            preserve_default=False,
        ),
    ]
