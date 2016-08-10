# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0021_auto_20150918_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f201',
            name='CTIZ',
            field=birth_registration.fields.CitizenshipField(blank=True, verbose_name='Citizenship', choices=[(1, '01 - Myanmar'), (2, '02 - Indian'), (3, '03 - Pakistani'), (4, '04 - Bangladesh'), (5, '05 - Nepalese'), (6, '06 - Chinese'), (7, '07 - European/American'), (8, '08 - Other Asian'), (9, '09 - Others'), (10, '10 - Not stated')]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='E_CODE',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='E-code of cause of death', choices=[('V', 'V'), ('W', 'W'), ('X', 'X'), ('Y', 'Y')]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='OCCU',
            field=birth_registration.fields.OccupationField(blank=True, verbose_name='Occupation', choices=[(1, '01 - Professional Technical and related workers'), (2, '02 - Administrative and managerial workers'), (3, '03 - Clerical and related workers'), (4, '04 - Sales workers'), (5, '05 - Services workers'), (6, '06 - Agriculture, Animal Husbandry and Forest workers, Fishermen, Hunters'), (7, '07 - Production and related workers, Transport equipment operators and labours'), (8, '08 - Not classified by occupation'), (9, '09 - Armed Forces'), (0, '00 - Economically inactive')]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='RACE',
            field=birth_registration.fields.RaceField(blank=True, verbose_name='Race', choices=[(1, '01 - Kachin'), (2, '02 - Kayah'), (3, '03 - Kayin'), (4, '04 - Chin'), (5, '05 - Bamar'), (6, '06 - Mon'), (7, '07 - Rakhine'), (8, '08 - Shan'), (9, '09 - Other indigenous Races'), (10, '10 - Myanmar/Foreigners'), (11, '11 - Chinese'), (12, '12 - Indian'), (13, '13 - Pakistani'), (14, '14 - Bangladesh'), (15, '15 - Nepal'), (16, '16 - Other Asian'), (17, '17 - Others'), (18, '18 - Not stated')]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='REL',
            field=birth_registration.fields.ReligionField(blank=True, verbose_name='Religion', choices=[(1, '01 - Buddhist'), (2, '02 - Islam'), (3, '03 - Christian'), (4, '04 - Hindu'), (5, '05 - Animist'), (6, '06 - Confucian'), (7, '07 - Sikh'), (8, '08 - Jew'), (9, '09 - Others'), (10, 'Not stated')]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='SEX',
            field=models.PositiveSmallIntegerField(verbose_name='Sex', choices=[(1, '01 - Male'), (2, '02 - Female'), (9, '09 - Not stated')]),
        ),
    ]
