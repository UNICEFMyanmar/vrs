# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0048_auto_20151114_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='f201',
            name='EXTRA_AGE_CODE',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='Extra age code', choices=[(b'1-1', '1-1'), (b'2-3', '2-3'), (b'3-2', '3-2'), (b'3-3', '3-3')]),
        ),
    ]
