# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0013_auto_20150902_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='f201',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 7, 12, 4, 17, 153942, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='f201',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='f201',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 7, 12, 4, 25, 349150, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
