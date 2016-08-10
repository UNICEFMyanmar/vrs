# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0004_auto_20150909_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='f103',
            name='NPLACE_B',
            field=birth_registration.fields.PlaceField(default=1, verbose_name='Place of Birth', choices=[(1, '01 - Home/House'), (2, '02 - Government Hospital'), (3, '03 - Nursing Home '), (4, '04 - Private Hospital/clinic'), (5, '05 - Other institution'), (6, '06 - Elsewhere')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='f103',
            name='NOPR',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='Registration Officer'),
        ),
        migrations.AlterField(
            model_name='f103',
            name='NSEX',
            field=models.PositiveSmallIntegerField(verbose_name='Sex', choices=[(1, '01 - Male'), (2, '02 - Female')]),
        ),
    ]
