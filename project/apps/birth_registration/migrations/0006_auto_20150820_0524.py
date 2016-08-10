# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0005_auto_20150818_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='f201',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='f201',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='f201',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='f201',
            name='E_CODE',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='E-code of cause of death', choices=[(1, 'V'), (2, 'W'), (3, 'X'), (4, 'Y')]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='f101',
            field=models.ForeignKey(blank=True, to='birth_registration.F101', null=True),
        ),
    ]
