# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0008_auto_20150912_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f103',
            name='Name_of_child',
            field=birth_registration.fields.Char100Field(default='', max_length=100, verbose_name='Name of child'),
            preserve_default=False,
        ),
    ]
