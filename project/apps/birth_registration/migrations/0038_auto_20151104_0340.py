# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0037_f201_age_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f201',
            name='AGE',
            field=birth_registration.fields.AGEfield(help_text='Note: If age is not stated in death information form do not code. (enquire later/make not of entry)', max_length=3, verbose_name='Age', choices=[(b'700', '700 - Newborn and under 1 hour'), (b'600', '600 - 1 - 11 hours'), (b'500', '500 - 12 hours and under 1 day'), (b'401', '401 - 1 days'), (b'402', '402 - 2 days'), (b'403', '403 - 3 days'), (b'404', '404 - 4 days'), (b'405', '405 - 5 days'), (b'406', '406 - 6 days'), (b'301', '301 - 1 weeks'), (b'302', '302 - 2 weeks'), (b'303', '303 - 3 weeks'), (b'201', '201 - 1 months'), (b'202', '202 - 2 months'), (b'203', '203 - 3 months'), (b'204', '204 - 4 months'), (b'205', '205 - 5 months'), (b'206', '206 - 6 months'), (b'207', '207 - 7 months'), (b'208', '208 - 8 months'), (b'209', '209 - 9 months'), (b'210', '210 - 10 months'), (b'211', '211 - 11 months'), (b'800', '800 - Unknown (under 1 year)'), (b'001', '001 - 1 years'), (b'002', '002 - 2 years'), (b'003', '003 - 3 years'), (b'004', '004 - 4 years'), (b'005', '005 - 5 years'), (b'006', '006 - 6 years'), (b'007', '007 - 7 years'), (b'008', '008 - 8 years'), (b'009', '009 - 9 years'), (b'010', '010 - 10 years'), (b'011', '011 - 11 years'), (b'012', '012 - 12 years'), (b'013', '013 - 13 years'), (b'014', '014 - 14 years'), (b'015', '015 - 15 years'), (b'016', '016 - 16 years'), (b'017', '017 - 17 years'), (b'018', '018 - 18 years'), (b'019', '019 - 19 years'), (b'020', '020 - 20 years'), (b'021', '021 - 21 years'), (b'022', '022 - 22 years'), (b'023', '023 - 23 years'), (b'024', '024 - 24 years'), (b'025', '025 - 25 years'), (b'026', '026 - 26 years'), (b'027', '027 - 27 years'), (b'028', '028 - 28 years'), (b'029', '029 - 29 years'), (b'030', '030 - 30 years'), (b'031', '031 - 31 years'), (b'032', '032 - 32 years'), (b'033', '033 - 33 years'), (b'034', '034 - 34 years'), (b'035', '035 - 35 years'), (b'036', '036 - 36 years'), (b'037', '037 - 37 years'), (b'038', '038 - 38 years'), (b'039', '039 - 39 years'), (b'040', '040 - 40 years'), (b'041', '041 - 41 years'), (b'042', '042 - 42 years'), (b'043', '043 - 43 years'), (b'044', '044 - 44 years'), (b'045', '045 - 45 years'), (b'046', '046 - 46 years'), (b'047', '047 - 47 years'), (b'048', '048 - 48 years'), (b'049', '049 - 49 years'), (b'050', '050 - 50 years'), (b'051', '051 - 51 years'), (b'052', '052 - 52 years'), (b'053', '053 - 53 years'), (b'054', '054 - 54 years'), (b'055', '055 - 55 years'), (b'056', '056 - 56 years'), (b'057', '057 - 57 years'), (b'058', '058 - 58 years'), (b'059', '059 - 59 years'), (b'060', '060 - 60 years'), (b'061', '061 - 61 years'), (b'062', '062 - 62 years'), (b'063', '063 - 63 years'), (b'064', '064 - 64 years'), (b'065', '065 - 65 years'), (b'066', '066 - 66 years'), (b'067', '067 - 67 years'), (b'068', '068 - 68 years'), (b'069', '069 - 69 years'), (b'070', '070 - 70 years'), (b'071', '071 - 71 years'), (b'072', '072 - 72 years'), (b'073', '073 - 73 years'), (b'074', '074 - 74 years'), (b'075', '075 - 75 years'), (b'076', '076 - 76 years'), (b'077', '077 - 77 years'), (b'078', '078 - 78 years'), (b'079', '079 - 79 years'), (b'080', '080 - 80 years'), (b'081', '081 - 81 years'), (b'082', '082 - 82 years'), (b'083', '083 - 83 years'), (b'084', '084 - 84 years'), (b'085', '085 - 85 years'), (b'086', '086 - 86 years'), (b'087', '087 - 87 years'), (b'088', '088 - 88 years'), (b'089', '089 - 89 years'), (b'090', '090 - 90 years'), (b'091', '091 - 91 years'), (b'092', '092 - 92 years'), (b'093', '093 - 93 years'), (b'094', '094 - 94 years'), (b'095', '095 - 95 years'), (b'096', '096 - 96 years'), (b'097', '097 - 97 years'), (b'098', '098 - 98 years'), (b'199', '199 - 99 years and over'), (b'900', '900 - Unknown (1 year and over )')]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='E_CODE',
            field=birth_registration.fields.E_CODEField(max_length=5, null=True, verbose_name='E-code of cause of death', choices=[('V', 'V'), ('W', 'W'), ('X', 'X'), ('Y', 'Y')]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='Father_name',
            field=birth_registration.fields.Char100Field(max_length=100, null=True, verbose_name="Father's name"),
        ),
        migrations.AlterField(
            model_name='f201',
            name='NRC',
            field=birth_registration.fields.Char100Field(max_length=100, null=True, verbose_name='NRC'),
        ),
        migrations.AlterField(
            model_name='f201',
            name='Name',
            field=birth_registration.fields.Char100Field(max_length=100, null=True, verbose_name='Name'),
        ),
    ]
