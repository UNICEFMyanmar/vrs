# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0045_auto_20151109_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='f201',
            name='N_CODE',
            field=birth_registration.fields.E_CODEField(max_length=6, null=True, verbose_name='N-Code'),
        ),
        migrations.AlterField(
            model_name='f201',
            name='E_CODE',
            field=birth_registration.fields.E_CODEField(max_length=6, null=True, verbose_name='E-Code'),
        ),
    ]
