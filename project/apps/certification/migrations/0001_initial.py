# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0015_auto_20150908_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='F103',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('f101', models.ForeignKey(to='birth_registration.F101')),
            ],
            options={
                'verbose_name': 'Form 103',
                'verbose_name_plural': 'Forms 103',
            },
        ),
    ]
