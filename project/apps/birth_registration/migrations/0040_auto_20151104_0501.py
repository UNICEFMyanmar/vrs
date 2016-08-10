# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0039_auto_20151104_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f201',
            name='DELI',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Was there a delivery', choices=[(1, '01 - Yes'), (2, '02 - No')]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='PRE',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='If a woman was the death associated with pregnancy', choices=[(1, '01 - Yes'), (2, '02 - No')]),
        ),
    ]
