# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0015_auto_20150908_1015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='f201',
            options={'verbose_name': 'Form 201', 'verbose_name_plural': 'Forms 201'},
        ),
        migrations.AlterField(
            model_name='f101',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 12, 10, 19, 0, 879819), editable=False),
        ),
    ]
