# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0015_auto_20150908_1015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='f201',
            options={'verbose_name': 'Form 201', 'verbose_name_plural': 'Forms 201'},
        ),
        migrations.AlterField(
            model_name='f201',
            name='E_CODE',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='E-code of cause of death', choices=[(1, 'V'), (2, 'W'), (3, 'X'), (4, 'Y')]),
        ),
    ]
