# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0021_auto_20151109_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f203',
            name='E_CODE',
            field=birth_registration.fields.E_CODEField(max_length=6, null=True, blank=True),
        ),
    ]
