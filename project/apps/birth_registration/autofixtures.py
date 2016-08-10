# -*- coding: utf-8 -*-
import random
import itertools
import datetime

from autofixture import AutoFixture
from autofixture import generators
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from birth_registration.codes import load_choices, CODES
from birth_registration.models import F101

State_Division_Choices, District_Choices, Township_or_town_Choices, Sub_code_No_Choices = load_choices(CODES)


def generate_triple():
    ST_DV, DIS, TWN = map(int, Permission.objects.filter(
        content_type=ContentType.objects.get(app_label="birth_registration", model="f101"),
        codename__regex=r'\d\d/\d\d/\d\d\d'
    ).order_by('?').first().codename.split("/"))
    return ST_DV, DIS, TWN


class FORMFixture(AutoFixture):
    def get_generator(self, field):
        if field.name in ('Original_form',):
            return None
        return super(FORMFixture, self).get_generator(field)


class F101Fixture(FORMFixture):

    class Values(object):

        ST_DV, DIS, TWN = generate_triple()
        RST_DV, RDIS, RTWN = generate_triple()
        CIR = 1
        NMULTI_B = generators.ChoicesGenerator(
            choices=list(itertools.chain.from_iterable(dict(F101.NMULTI_B_CHOICES).values())))

    def post_process_instance(self, instance, commit):

        if instance.NR_AREA == 1:
            instance.RHC = None

        instance.created_at = datetime.date.today() - datetime.timedelta(days=random.randint(0, 31))
        instance.ST_DV, instance.DIS, instance.TWN = generate_triple()

        if commit:
            instance.save()
        return instance


class F201Fixture(FORMFixture):
    class Values(object):
        NNRT, NNRT1, NNST = generate_triple()

    def post_process_instance(self, instance, commit):
        instance.created_at = datetime.date.today() - datetime.timedelta(days=random.randint(0, 31))
        instance.NNRT, instance.NNRT1, instance.NNST = generate_triple()

        if commit:
            instance.save()
        return instance
