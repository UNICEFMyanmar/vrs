# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0010_auto_20150828_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f201',
            name='AGE',
            field=models.CharField(help_text='<ul><li>Newborn and under 1 hour 700</li><li>1 \u2013 11 hours 600</li><li>12 hours and under 1 day 500</li><li>1 day 401</li><li>2 days 402</li><li>3 days 403</li><li>and so on......</li><li>7 days and 1 week 301</li><li>2 weeks 302</li><li>3 weeks 303</li><li>4 weeks and under 1 months 201</li><li>2 months 202</li><li>3 months 203</li><li>and so on......</li><li></li><li>10 months 210</li><li>11 months 211</li><li>unknown (under 1 year of age 800</li><li>1 year 001</li><li>2 years 002</li><li>3 years 003</li><li>and so on.....</li><li>10 years 010</li><li>11 years 011</li><li>12 yaers 012</li><li>and so on.....</li><li>99 and over 199</li><li>unknown (1 year and over 900 Note: If age is not stated in death information form do not code. (enquire later/ make not of entry)</li></ul>', max_length=3, verbose_name='Age', blank=True),
        ),
        migrations.AlterField(
            model_name='f201',
            name='SEX',
            field=models.PositiveSmallIntegerField(help_text='<ul><li>Male = 1 </li><li>Female = 2 </li><li>Not stated = 9</li></ul>', choices=[(1, '01 - Male'), (2, '02 - Female'), (9, '09 - Not stated')], verbose_name='Sex', validators=[django.core.validators.RegexValidator(regex=b'(1|2|9)', message='Incorrect choice. Avaiable choices:1 - Male, 2 - Female9 - Not Stated.')]),
        ),
    ]
