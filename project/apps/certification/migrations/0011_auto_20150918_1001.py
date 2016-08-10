# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.models
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0010_auto_20150918_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f103',
            name='CIR',
            field=birth_registration.fields.CIRfield(blank=True, help_text=('Code 01 for vital events occurred in any hospital and 21,22,23,...99 for any hospital in Yangon City',), null=True, verbose_name='Sub code No (urban areas)', choices=[(1, '1 - Any hospital'), ('01 - Thingankyun', [(21, '21 - Thingangyun Model Hospital')]), ('03 - Taung Okkalapa', [(22, '22 - Women and Children Hospital')]), ('04 - Myauk Okkalapa', [(23, '23 - Myauk Okklapa Hospital'), (28, '28 - Myauk Okklapa Hospital for infectious diseases (Waibargi)')]), ('05 - Tharketa', [(24, '24 - Tharketa township hospital')]), ('07 - Tarmwe', [(25, '25 - Hospital for eyes and optical')]), ('09 - Botahtaung', [(26, '26 - Eastern Yangon General Hospital')]), ('14 - Mingalataungnyunt', [(27, '27 - Hospital for workers')]), ('03 - Lanmadaw', [(29, '29 - Central Women Hospital'), (30, '30 - Children Hospital')]), ('04 - Lathar', [(31, '31 - Yangon General Hospital'), (32, '32 - New Yangon General Hospital (Japan)')]), ('06 - Kyeemyindine', [(33, '33 - Western Yangon General Hospital'), (34, '34 - Ortho Hospital (Kyeemyindine)')]), ('10 - Mayangone', [(35, '35 - Psychiatric Hospital')]), ('11 - Dagon', [(36, '36 - No.2 Military Hospital (Dagon)')]), ('12 - Bahan', [(37, '37 - Towerlane Women Hospital (Bahan)')]), ('01 - Insein', [(39, '39 - Insein Railway Hospital'), (40, '40 - Aungsan Hospital for Lung Diseases')]), ('02 - Mingalardon', [(41, '41 - No.1 Military Hospital (Mingalardon)')]), (99, '99 - Not mentioned')]),
        ),
        migrations.AlterField(
            model_name='f103',
            name='RHC',
            field=birth_registration.models.RHCfield(blank=True, to='birth_registration.RHC', help_text='RHC code (rural areas)', null=True),
        ),
    ]
