# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0009_auto_20150827_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f101',
            name='NPRV_CH',
            field=models.PositiveSmallIntegerField(blank=True, help_text='99 - Not stated', null=True, verbose_name="Mother's previous children (Excluding this one)", validators=[django.core.validators.MaxValueValidator(99)]),
        ),
    ]
