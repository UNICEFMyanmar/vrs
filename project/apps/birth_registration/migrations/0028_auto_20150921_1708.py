# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0027_auto_20150921_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f101',
            name='NCZN_M',
            field=birth_registration.fields.CitizenshipField(blank=True, null=True, verbose_name="Mother's citizenship", choices=[(1, '01 - Myanmar'), (2, '02 - Indian'), (3, '03 - Pakistani'), (4, '04 - Bangladesh'), (5, '05 - Nepalese'), (6, '06 - Chinese'), (7, '07 - European/American'), (8, '08 - Other Asian'), (9, '09 - Others'), (10, '10 - Not stated')]),
        ),
    ]
