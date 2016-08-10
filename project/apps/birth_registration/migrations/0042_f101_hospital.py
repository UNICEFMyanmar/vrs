# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0041_auto_20151109_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='f101',
            name='Hospital',
            field=models.ForeignKey(blank=True, editable=False, to='birth_registration.Hospital', null=True),
        ),
    ]
