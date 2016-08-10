# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import birth_registration.fields
import birth_registration.validators


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0046_auto_20151114_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f201',
            name='N_CODE',
            field=birth_registration.fields.N_CODEField(max_length=6, null=True, verbose_name='N-Code', validators=[birth_registration.validators.validate_E_CODE]),
        ),
    ]
