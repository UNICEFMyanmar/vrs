# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import birth_registration.fields
import birth_registration.validators


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0047_auto_20151114_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f201',
            name='E_CODE',
            field=birth_registration.fields.E_CODEField(validators=[birth_registration.validators.validate_E_CODE], max_length=6, blank=True, help_text='V99.99', null=True, verbose_name='E-Code'),
        ),
    ]
