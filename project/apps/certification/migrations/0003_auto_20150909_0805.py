# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import birth_registration.fields
from django.utils.timezone import utc
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('birth_registration', '0015_auto_20150908_1015'),
        ('certification', '0002_auto_20150908_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='f103',
            name='Date_of_Birth',
            field=models.DateField(default=datetime.datetime(2015, 9, 9, 13, 4, 34, 755750, tzinfo=utc), help_text='Day, month and year: <kbd>25102006</kbd>', verbose_name='Date of Birth'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='f103',
            name='Date_of_Registration',
            field=models.DateField(default=datetime.datetime(2015, 9, 9, 13, 4, 42, 681113, tzinfo=utc), help_text='Day, month and year: <kbd>25102006</kbd>', verbose_name='Date of Registration'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='f103',
            name='Father_NRC',
            field=birth_registration.fields.Char100Field(max_length=100, null=True, verbose_name="Father's NRC", blank=True),
        ),
        migrations.AddField(
            model_name='f103',
            name='Father_name',
            field=birth_registration.fields.Char100Field(max_length=100, null=True, verbose_name="Father's Name", blank=True),
        ),
        migrations.AddField(
            model_name='f103',
            name='Informer',
            field=birth_registration.fields.Char300Field(max_length=300, null=True, verbose_name="Informer's name and address", blank=True),
        ),
        migrations.AddField(
            model_name='f103',
            name='Mother_NRC',
            field=birth_registration.fields.Char100Field(max_length=100, null=True, verbose_name="Mother's NRC", blank=True),
        ),
        migrations.AddField(
            model_name='f103',
            name='Mother_name',
            field=birth_registration.fields.Char100Field(max_length=100, null=True, verbose_name="Mother's Name"),
        ),
        migrations.AddField(
            model_name='f103',
            name='NCZN_F',
            field=birth_registration.fields.CitizenshipField(blank=True, choices=[(1, '01 - Myanmar'), (2, '02 - Indian'), (3, '03 - Pakistani'), (4, '04 - Bangladesh'), (5, '05 - Nepalese'), (6, '06 - Chinese'), (7, '07 - European/American'), (8, '08 - Other Asian'), (9, '09 - Others'), (10, '10 - Not stated')], null=True, verbose_name="Father's Citizenship", validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='f103',
            name='NCZN_M',
            field=birth_registration.fields.CitizenshipField(blank=True, choices=[(1, '01 - Myanmar'), (2, '02 - Indian'), (3, '03 - Pakistani'), (4, '04 - Bangladesh'), (5, '05 - Nepalese'), (6, '06 - Chinese'), (7, '07 - European/American'), (8, '08 - Other Asian'), (9, '09 - Others'), (10, '10 - Not stated')], null=True, verbose_name='Usual Place of residence of mother:', validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='f103',
            name='NOCC_F',
            field=birth_registration.fields.OccupationField(blank=True, null=True, verbose_name="Father's Occupation", choices=[(1, '01 - Professional Technical and related workers'), (2, '02 - Administrative and managerial workers'), (3, '03 - Clerical and related workers'), (4, '04 - Sales workers'), (5, '05 - Services workers'), (6, '06 - Agriculture, Animal Husbandry and Forest workers, Fishermen, Hunters'), (7, '07 - Production and related workers, Transport equipment operators and labours'), (8, '08 - Not classified by occupation'), (9, '09 - Armed Forces'), (0, '00 - Economically inactive')]),
        ),
        migrations.AddField(
            model_name='f103',
            name='NOCC_M',
            field=birth_registration.fields.OccupationField(blank=True, null=True, verbose_name="Mother's occupation", choices=[(1, '01 - Professional Technical and related workers'), (2, '02 - Administrative and managerial workers'), (3, '03 - Clerical and related workers'), (4, '04 - Sales workers'), (5, '05 - Services workers'), (6, '06 - Agriculture, Animal Husbandry and Forest workers, Fishermen, Hunters'), (7, '07 - Production and related workers, Transport equipment operators and labours'), (8, '08 - Not classified by occupation'), (9, '09 - Armed Forces'), (0, '00 - Economically inactive')]),
        ),
        migrations.AddField(
            model_name='f103',
            name='NOPR',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='f103',
            name='NRACE_F',
            field=birth_registration.fields.RaceField(blank=True, null=True, verbose_name="Father's Race", choices=[(1, '01 - Kachin'), (2, '02 - Kayah'), (3, '03 - Kayin'), (4, '04 - Chin'), (5, '05 - Bamar'), (6, '06 - Mon'), (7, '07 - Rakhine'), (8, '08 - Shan'), (9, '09 - Other indigenous Races'), (10, '10 - Myanmar/Foreigners'), (11, '11 - Chinese'), (12, '12 - Indian'), (13, '13 - Pakistani'), (14, '14 - Bangladesh'), (15, '15 - Nepal'), (16, '16 - Other Asian'), (17, '17 - Others'), (18, '18 - Not stated')]),
        ),
        migrations.AddField(
            model_name='f103',
            name='NRACE_M',
            field=birth_registration.fields.RaceField(blank=True, null=True, verbose_name="Mother's Race", choices=[(1, '01 - Kachin'), (2, '02 - Kayah'), (3, '03 - Kayin'), (4, '04 - Chin'), (5, '05 - Bamar'), (6, '06 - Mon'), (7, '07 - Rakhine'), (8, '08 - Shan'), (9, '09 - Other indigenous Races'), (10, '10 - Myanmar/Foreigners'), (11, '11 - Chinese'), (12, '12 - Indian'), (13, '13 - Pakistani'), (14, '14 - Bangladesh'), (15, '15 - Nepal'), (16, '16 - Other Asian'), (17, '17 - Others'), (18, '18 - Not stated')]),
        ),
        migrations.AddField(
            model_name='f103',
            name='NREL_F',
            field=birth_registration.fields.ReligionField(blank=True, choices=[(1, '01 - Buddhist'), (2, '02 - Islam'), (3, '03 - Christian'), (4, '04 - Hindu'), (5, '05 - Animist'), (6, '06 - Confucion'), (7, '07 - Sikh'), (8, '08 - Jew'), (9, '09 - Others'), (10, 'Not stated')], null=True, verbose_name="Father's Religion", validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='f103',
            name='NREL_M',
            field=birth_registration.fields.ReligionField(blank=True, choices=[(1, '01 - Buddhist'), (2, '02 - Islam'), (3, '03 - Christian'), (4, '04 - Hindu'), (5, '05 - Animist'), (6, '06 - Confucion'), (7, '07 - Sikh'), (8, '08 - Jew'), (9, '09 - Others'), (10, 'Not stated')], null=True, verbose_name="Mother's Religion", validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='f103',
            name='NR_SNO',
            field=birth_registration.fields.SerialNoField(default=1, help_text='Enter serial No. direct into coding column. Watch carefully for sequence of serial No. If it is not in sequence make query.<br/>Code actual serial No. in full to 5 digits. If serial No. is 1 to 99; Code 00001-00009, and 10-99 code 00010, 00011,\u2026\u2026\u202600099, 00100 and over in full', verbose_name='Serial No. in Registration book', validators=[django.core.validators.MaxValueValidator(99999)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='f103',
            name='NSEX',
            field=models.PositiveSmallIntegerField(default=1, help_text='<ul><li>Male = 1 </li><li>Female = 2 </li></ul>', verbose_name='Sex', choices=[(1, '01 - Male'), (2, '02 - Female')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='f103',
            name='Name_of_child',
            field=birth_registration.fields.Char100Field(help_text='(if has)', max_length=100, null=True, verbose_name='Name of child', blank=True),
        ),
        migrations.AddField(
            model_name='f103',
            name='RCIR',
            field=birth_registration.fields.Char300Field(max_length=300, null=True, verbose_name="Mother's Address", blank=True),
        ),
        migrations.AddField(
            model_name='f103',
            name='RHC',
            field=models.ForeignKey(blank=True, to='birth_registration.RHC', null=True),
        ),
        migrations.AddField(
            model_name='f103',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 9, 13, 4, 59, 994430, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='f103',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='f103',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 9, 13, 5, 3, 405642, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
