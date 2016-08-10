# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0044_auto_20151109_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='f201',
            name='Hospital',
            field=models.ForeignKey(blank=True, to='birth_registration.Hospital', null=True),
        ),
        migrations.AddField(
            model_name='f201',
            name='governmental_hospital',
            field=birth_registration.fields.Char100Field(max_length=100, null=True, verbose_name='Governmental hospital name', blank=True),
        ),
        migrations.AddField(
            model_name='f201',
            name='private_hospital',
            field=birth_registration.fields.Char100Field(max_length=100, null=True, verbose_name='Private hospital name', blank=True),
        ),
    ]
