# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0016_auto_20150912_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f101',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 12, 15, 3, 36, 49775), editable=False),
        ),
        migrations.AlterField(
            model_name='f201',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 12, 15, 3, 36, 72812), editable=False),
        ),
    ]
