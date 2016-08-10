# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0015_f103_nczn_m'),
    ]

    operations = [
        migrations.AddField(
            model_name='f203',
            name='RCIR',
            field=models.TextField(null=True, verbose_name='Usual place of residence', blank=True),
        ),
        migrations.AlterField(
            model_name='f203',
            name='Informant_name',
            field=models.TextField(null=True, verbose_name="Informant's name, address and relationship to deceased", blank=True),
        ),
    ]
