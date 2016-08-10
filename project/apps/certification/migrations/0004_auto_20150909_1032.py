# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0003_auto_20150909_0805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='f103',
            name='Father_NRC',
        ),
        migrations.RemoveField(
            model_name='f103',
            name='Mother_NRC',
        ),
        migrations.RemoveField(
            model_name='f103',
            name='NCZN_M',
        ),
        migrations.RemoveField(
            model_name='f103',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='f103',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='f103',
            name='Date_of_Birth',
            field=models.DateField(verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='f103',
            name='Date_of_Registration',
            field=models.DateField(verbose_name='Date of Registration'),
        ),
        migrations.AlterField(
            model_name='f103',
            name='Informer',
            field=models.TextField(null=True, verbose_name="Informer's name and address", blank=True),
        ),
        migrations.AlterField(
            model_name='f103',
            name='NR_SNO',
            field=birth_registration.fields.SerialNoField(verbose_name='Serial No. in Registration book', validators=[django.core.validators.MaxValueValidator(99999)]),
        ),
        migrations.AlterField(
            model_name='f103',
            name='NSEX',
            field=models.PositiveSmallIntegerField(verbose_name='Sex'),
        ),
        migrations.AlterField(
            model_name='f103',
            name='Name_of_child',
            field=birth_registration.fields.Char100Field(max_length=100, null=True, verbose_name='Name of child', blank=True),
        ),
        migrations.AlterField(
            model_name='f103',
            name='RCIR',
            field=models.TextField(null=True, verbose_name="Mother's Address", blank=True),
        ),
    ]
