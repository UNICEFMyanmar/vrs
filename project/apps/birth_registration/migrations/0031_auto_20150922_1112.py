# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0030_auto_20150921_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='f201',
            name='RCIR',
            field=birth_registration.fields.Char300Field(max_length=300, null=True, verbose_name='Usual place of residence', blank=True),
        ),
        migrations.AlterField(
            model_name='f201',
            name='Date_of_Registration',
            field=models.DateField(help_text='Day, month and year: <kbd>25102006</kbd>', verbose_name='Date of Registration'),
        ),
    ]
