# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields
import birth_registration.validators


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0026_auto_20150921_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f101',
            name='Father_name',
            field=birth_registration.fields.Char100Field(max_length=100, null=True, verbose_name="Father's name", blank=True),
        ),
        migrations.AlterField(
            model_name='f101',
            name='Mother_name',
            field=birth_registration.fields.Char100Field(max_length=100, null=True, verbose_name="Mother's name"),
        ),
        migrations.AlterField(
            model_name='f101',
            name='NCZN_F',
            field=birth_registration.fields.CitizenshipField(blank=True, null=True, verbose_name="Father's citizenship", choices=[(1, '01 - Myanmar'), (2, '02 - Indian'), (3, '03 - Pakistani'), (4, '04 - Bangladesh'), (5, '05 - Nepalese'), (6, '06 - Chinese'), (7, '07 - European/American'), (8, '08 - Other Asian'), (9, '09 - Others'), (10, '10 - Not stated')]),
        ),
        migrations.AlterField(
            model_name='f101',
            name='NOCC_F',
            field=birth_registration.fields.OccupationField(blank=True, null=True, verbose_name="Father's occupation", choices=[(1, '01 - Professional Technical and related workers'), (2, '02 - Administrative and managerial workers'), (3, '03 - Clerical and related workers'), (4, '04 - Sales workers'), (5, '05 - Services workers'), (6, '06 - Agriculture, Animal Husbandry and Forest workers, Fishermen, Hunters'), (7, '07 - Production and related workers, Transport equipment operators and labours'), (8, '08 - Not classified by occupation'), (9, '09 - Armed Forces'), (0, '00 - Economically inactive')]),
        ),
        migrations.AlterField(
            model_name='f101',
            name='NRACE_F',
            field=birth_registration.fields.RaceField(blank=True, null=True, verbose_name="Father's race", choices=[(1, '01 - Kachin'), (2, '02 - Kayah'), (3, '03 - Kayin'), (4, '04 - Chin'), (5, '05 - Bamar'), (6, '06 - Mon'), (7, '07 - Rakhine'), (8, '08 - Shan'), (9, '09 - Other indigenous Races'), (10, '10 - Myanmar/Foreigners'), (11, '11 - Chinese'), (12, '12 - Indian'), (13, '13 - Pakistani'), (14, '14 - Bangladesh'), (15, '15 - Nepal'), (16, '16 - Other Asian'), (17, '17 - Others'), (18, '18 - Not stated')]),
        ),
        migrations.AlterField(
            model_name='f101',
            name='NRACE_M',
            field=birth_registration.fields.RaceField(blank=True, null=True, verbose_name="Mother's race", choices=[(1, '01 - Kachin'), (2, '02 - Kayah'), (3, '03 - Kayin'), (4, '04 - Chin'), (5, '05 - Bamar'), (6, '06 - Mon'), (7, '07 - Rakhine'), (8, '08 - Shan'), (9, '09 - Other indigenous Races'), (10, '10 - Myanmar/Foreigners'), (11, '11 - Chinese'), (12, '12 - Indian'), (13, '13 - Pakistani'), (14, '14 - Bangladesh'), (15, '15 - Nepal'), (16, '16 - Other Asian'), (17, '17 - Others'), (18, '18 - Not stated')]),
        ),
        migrations.AlterField(
            model_name='f101',
            name='RCIR',
            field=birth_registration.fields.Char300Field(max_length=300, null=True, verbose_name='Address of mother', blank=True),
        ),
        migrations.AlterField(
            model_name='f101',
            name='RST_DV',
            field=birth_registration.fields.StateDivisionField(validators=[birth_registration.validators.validate_2digits], choices=[(1, '01 - Kachin'), (2, '02 - Kayh'), (3, '03 - Kayin'), (4, '04 - Chin'), (5, '05 - Sagaing'), (6, '06 - Tanintharyi'), (7, '07 - Bago'), (8, '08 - Magway'), (9, '09 - Mandalay'), (10, '10 - Mon'), (11, '11 - Rakhine'), (12, '12 - Yangon'), (13, '13 - Shan'), (14, '14 - Ayyarwaddy'), (15, '15 - NayPyiTaw')], blank=True, help_text='State Division', null=True, verbose_name='Usual Place of residence of mother:'),
        ),
    ]
