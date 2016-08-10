# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0038_auto_20151104_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f101',
            name='Informer',
            field=birth_registration.fields.Char300Field(max_length=300, null=True, verbose_name="Informer's name, address and relation to the child:", blank=True),
        ),
    ]
