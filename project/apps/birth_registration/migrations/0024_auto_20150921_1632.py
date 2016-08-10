# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0023_auto_20150921_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f201',
            name='CERT',
            field=birth_registration.fields.CERTField(blank=True, null=True, verbose_name='Person certifying cause of death', choices=[(1, '01 - Registered doctor in attendance'), (2, '02- Medical Registrar'), (3, '03 - Other Registered doctor not in attendance'), (4, '04 - Health Assistant'), (5, '05 - Other Health personnel'), (6, '06 - Others')]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='E_CODE',
            field=birth_registration.fields.E_CODEField(blank=True, max_length=5, null=True, verbose_name='E-code of cause of death', choices=[('V', 'V'), ('W', 'W'), ('X', 'X'), ('Y', 'Y')]),
        ),
    ]
