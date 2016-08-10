# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0007_auto_20150827_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='f201',
            name='OPR',
        ),
        migrations.RemoveField(
            model_name='f201',
            name='RHC',
        ),
    ]
