# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields
import django.core.validators
import birth_registration.validators


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0028_auto_20150921_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f101',
            name='NB_ALIV',
            field=models.PositiveSmallIntegerField(help_text='99 - Not Stated', null=True, verbose_name='Number born alive (Excluding this one)', blank=True),
        ),
        migrations.AlterField(
            model_name='f101',
            name='NPRV_CH',
            field=models.PositiveSmallIntegerField(blank=True, help_text='99 - Not Stated', null=True, verbose_name="Mother's previous children (Excluding this one)", validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='f101',
            name='PERIOD',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Code 2 digits in week', null=True, verbose_name='Gestational period', validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='f101',
            name='RST_DV',
            field=birth_registration.fields.StateDivisionField(validators=[birth_registration.validators.validate_2digits], choices=[(1, '01 - Kachin'), (2, '02 - Kayh'), (3, '03 - Kayin'), (4, '04 - Chin'), (5, '05 - Sagaing'), (6, '06 - Tanintharyi'), (7, '07 - Bago'), (8, '08 - Magway'), (9, '09 - Mandalay'), (10, '10 - Mon'), (11, '11 - Rakhine'), (12, '12 - Yangon'), (13, '13 - Shan'), (14, '14 - Ayyarwaddy'), (15, '15 - NayPyiTaw')], blank=True, help_text=' State Division', null=True, verbose_name='Usual Place of residence of mother:'),
        ),
    ]
