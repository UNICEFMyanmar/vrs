# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0009_auto_20150918_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f103',
            name='NCZN_F',
            field=birth_registration.fields.CitizenshipField(blank=True, null=True, verbose_name="Father's Citizenship", choices=[(1, '01 - Myanmar'), (2, '02 - Indian'), (3, '03 - Pakistani'), (4, '04 - Bangladesh'), (5, '05 - Nepalese'), (6, '06 - Chinese'), (7, '07 - European/American'), (8, '08 - Other Asian'), (9, '09 - Others'), (10, '10 - Not stated')]),
        ),
        migrations.AlterField(
            model_name='f103',
            name='NREL_F',
            field=birth_registration.fields.ReligionField(blank=True, null=True, verbose_name="Father's Religion", choices=[(1, '01 - Buddhist'), (2, '02 - Islam'), (3, '03 - Christian'), (4, '04 - Hindu'), (5, '05 - Animist'), (6, '06 - Confucion'), (7, '07 - Sikh'), (8, '08 - Jew'), (9, '09 - Others'), (10, 'Not stated')]),
        ),
        migrations.AlterField(
            model_name='f103',
            name='NREL_M',
            field=birth_registration.fields.ReligionField(blank=True, null=True, verbose_name="Mother's Religion", choices=[(1, '01 - Buddhist'), (2, '02 - Islam'), (3, '03 - Christian'), (4, '04 - Hindu'), (5, '05 - Animist'), (6, '06 - Confucion'), (7, '07 - Sikh'), (8, '08 - Jew'), (9, '09 - Others'), (10, 'Not stated')]),
        ),
    ]
