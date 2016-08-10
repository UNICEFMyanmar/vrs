# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0036_f201_nrc'),
    ]

    operations = [
        migrations.AddField(
            model_name='f201',
            name='AGE_CODE',
            field=models.SmallIntegerField(null=True, verbose_name='Age code', blank=True),
        ),
    ]
