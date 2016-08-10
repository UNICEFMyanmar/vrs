# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0042_f101_hospital'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='Birth_registration',
            new_name='birth',
        ),
        migrations.RenameField(
            model_name='hospital',
            old_name='Code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='hospital',
            old_name='Death_registration',
            new_name='death',
        ),
        migrations.RenameField(
            model_name='hospital',
            old_name='Name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='f101',
            name='Hospital',
            field=models.ForeignKey(blank=True, to='birth_registration.Hospital', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='hospital',
            unique_together=set([('ST_DV', 'DIS', 'TWN', 'code')]),
        ),
    ]
