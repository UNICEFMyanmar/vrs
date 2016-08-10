# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0022_auto_20151114_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='f203',
            name='AGE',
        ),
        migrations.AddField(
            model_name='f203',
            name='AGE_GROUP',
            field=birth_registration.fields.AgeGroupField(default=99, help_text='Age group for cause of death', verbose_name='Age Group', choices=[(0, '0 - Under 1 year'), (1, '1 - 1 year'), (2, '2 - 2 years'), (3, '3 - 3 years'), (4, '4 - 4 years'), (5, '6 - 5-9 years'), (6, '7 - 10-14 years'), (7, '8 - 15-19 years'), (8, '9 - 20-24 years'), (9, '10 - 25-29 years'), (10, '11 - 30-34 years'), (11, '12 - 35-39 years'), (12, '13 - 40-44 years'), (13, '14 - 45-49 years'), (14, '15 - 50-54 years'), (15, '16 - 55-59 years'), (16, '17 - 60-64 years'), (17, '18 - 65-69 years'), (18, '19 - 70-74 years'), (19, '20 - 75-79 years'), (20, '21 - 80-84 years'), (21, '22 - 85 and over'), (99, '23 - No stated')]),
        ),
    ]
