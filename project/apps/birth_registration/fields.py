# -*- coding: utf-8 -*-
import os
import datetime
import uuid
from django.db import models
from django.utils.encoding import force_text, force_str
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator

from .codes import load_choices, CODES, URBAN, RURAL, \
    SEX_FEMALE, SEX_NOT_STATED, SEX_MALE
from .validators import validate_2digits, validate_E_CODE, validate_N_CODE

State_Division_Choices, District_Choices, Township_or_town_Choices, Sub_code_No_Choices = load_choices(CODES)


def make_image_path(instance, filename):
    path = os.path.normpath(force_text(datetime.datetime.now().strftime(force_str('%Y/%m/%d/'))))
    new_filename = "%s_%s" % (uuid.uuid4(), filename)

    return os.path.join(instance.__class__.__name__.lower(), path, new_filename)


def get_township(code):
    for district, townships in Township_or_town_Choices:
        for tcode, township in townships:
            if code == tcode:
                return township


class StateDivisionField(models.PositiveSmallIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [validate_2digits]
        kwargs['choices'] = State_Division_Choices
        super(StateDivisionField, self).__init__(*args, **kwargs)


class DistrictField(models.PositiveSmallIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [validate_2digits, ]
        kwargs['choices'] = District_Choices
        super(DistrictField, self).__init__(*args, **kwargs)


class TownshipField(models.PositiveSmallIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = Township_or_town_Choices
        super(TownshipField, self).__init__(*args, **kwargs)


class AreaField(models.PositiveSmallIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = (
            (URBAN, _(u'01 - Urban')),
            (RURAL, _(u'02 - Rural')),
        )
        kwargs['help_text'] = _(u'Urban/Rural')
        super(AreaField, self).__init__(*args, **kwargs)


class CIRfield(models.PositiveSmallIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = _(u'Sub code No (urban areas)')
        kwargs['help_text'] = _(u"Code 01 for vital events occurred in any hospital and 21,22,23,...99 "
                                u"for any hospital in Yangon City")
        kwargs['choices'] = Sub_code_No_Choices
        super(CIRfield, self).__init__(*args, **kwargs)


class SerialNoField(models.PositiveIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = _(u"Serial number in registration book")
        kwargs['help_text'] = _(
            u'Enter serial No. direct into coding column. '
            u'Watch carefully for sequence of serial No. '
            u'If it is not in sequence make query.<br/>'
            u'Code actual serial No. in full to 5 digits. '
            u'If serial No. is 1 to 99; Code 00001-00009, '
            u'and 10-99 code 00010, 00011,………00099, 00100 and over in full'
        )

        kwargs['validators'] = [MaxValueValidator(99999), ]
        super(SerialNoField, self).__init__(*args, **kwargs)


class AgeGroupField(models.SmallIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['help_text'] = _(u'Age group for cause of death')

        kwargs['choices'] = (
            (0, _(u'0 - Under 1 year')),
            (1, _(u'1 - 1 year')),
            (2, _(u'2 - 2 years')),
            (3, _(u'3 - 3 years')),
            (4, _(u'4 - 4 years')),
            (5, _(u'6 - 5-9 years')),
            (6, _(u'7 - 10-14 years')),
            (7, _(u'8 - 15-19 years')),
            (8, _(u'9 - 20-24 years')),
            (9, _(u'10 - 25-29 years')),
            (10, _(u'11 - 30-34 years')),
            (11, _(u'12 - 35-39 years')),
            (12, _(u'13 - 40-44 years')),
            (13, _(u'14 - 45-49 years')),
            (14, _(u'15 - 50-54 years')),
            (15, _(u'16 - 55-59 years')),
            (16, _(u'17 - 60-64 years')),
            (17, _(u'18 - 65-69 years')),
            (18, _(u'19 - 70-74 years')),
            (19, _(u'20 - 75-79 years')),
            (20, _(u'21 - 80-84 years')),
            (21, _(u'22 - 85 and over')),
            (99, _(u'23 - No stated'))
        )
        super(AgeGroupField, self).__init__(*args, **kwargs)


class AGEfield(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 3
        kwargs['verbose_name'] = _(u'Age')
        kwargs['help_text'] = _(u'Note: If age is not stated in death information form do not code. '
                                u'(enquire later/make not of entry)')
        kwargs['choices'] = (
                                ("700", _(u"700 - Newborn and under 1 hour")),
                                ("600", _(u"600 - 1 - 11 hours")),
                                ("500", _(u"500 - 12 hours and under 1 day"))) + \
                            tuple([(str(x), _(u"%d - %s days" % (x, x - 400))) for x in range(401, 407)]) + \
                            tuple([(str(x), _(u"%d - %s weeks") % (x, x - 300)) for x in range(301, 304)]) + \
                            tuple([(str(x), _(u"%d - %s months") % (x, x - 200)) for x in range(201, 212)]) + \
                            tuple([("800", _(u"800 - Unknown (under 1 year)"))]) + \
                            tuple([(str(x).zfill(3), _(u"%s - %d years") % (str(x).zfill(3), x),) for x in
                                   range(1, 99)]) + \
                            tuple([("199", _(u"199 - 99 years and over")),
                                   ("900", _(u"900 - Unknown (1 year and over )"))])

        super(AGEfield, self).__init__(*args, **kwargs)


class E_CODEField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [validate_E_CODE]
        kwargs['max_length'] = 6
        kwargs['help_text'] = _(u'V99.99')
        super(E_CODEField, self).__init__(*args, **kwargs)


class N_CODEField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [validate_N_CODE]
        kwargs['max_length'] = 6
        kwargs['help_text'] = _(u'A99.99')
        super(N_CODEField, self).__init__(*args, **kwargs)


class SEXField(models.PositiveSmallIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = _(u"Sex")
        kwargs['choices'] = (
            (SEX_MALE, _(u'01 - Male')),
            (SEX_FEMALE, _(u'02 - Female')),
            (SEX_NOT_STATED, _(u'09 - Not stated'))
        )
        super(SEXField, self).__init__(*args, **kwargs)


class CERTField(models.PositiveSmallIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = _(u'Person certifying cause of death')
        kwargs['choices'] = (
            (1, _(u'01 - Registered doctor in attendance')),
            (2, _(u'02 - Registered doctor Not in Attendance')),
            (3, _(u'03 - Health Officer')),
            (4, _(u'04 - Other Health Staffs')),
            (4, _(u'05 - Other')),
        )
        super(CERTField, self).__init__(*args, **kwargs)


class PlaceField(models.PositiveSmallIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = (
            (1, _(u'01 - Home/House')),
            (2, _(u'02 - Government Hospital')),
            (3, _(u'03 - Nursing Home (including any maternity and child welfare society) ')),
            (4, _(u'04 - Private Hospital/clinic')),
            (5, _(u'05 - Other institution')),
        )
        super(PlaceField, self).__init__(*args, **kwargs)


class RaceField(models.PositiveSmallIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = (
            (1, _(u'01 - Kachin')),
            (2, _(u'02 - Kayah')),
            (3, _(u'03 - Kayin')),
            (4, _(u'04 - Chin')),
            (5, _(u'05 - Bamar')),
            (6, _(u'06 - Mon')),
            (7, _(u'07 - Rakhine')),
            (8, _(u'08 - Shan')),
            (9, _(u'09 - Other indigenous Races')),
            (10, _(u'10 - Myanmar/Foreigners')),
            (11, _(u'11 - Chinese')),
            (12, _(u'12 - Indian')),
            (13, _(u'13 - Pakistani')),
            (14, _(u'14 - Bangladesh')),
            (15, _(u'15 - Nepal')),
            (16, _(u'16 - Other Asian')),
            (17, _(u'17 - Others')),
            (18, _(u'18 - Not stated'))
        )
        super(RaceField, self).__init__(*args, **kwargs)


class OccupationField(models.PositiveSmallIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = (
            (1, _(u'01 - Professional Technical and related workers')),
            (2, _(u'02 - Administrative and managerial workers')),
            (3, _(u'03 - Clerical and related workers')),
            (4, _(u'04 - Sales workers')),
            (5, _(u'05 - Services workers')),
            (6, _(u'06 - Agriculture, Animal Husbandry and Forest workers, Fishermen, Hunters')),
            (7, _(u'07 - Production and related workers, Transport equipment operators and labours')),
            (8, _(u'08 - Not classified by occupation')),
            (9, _(u'09 - Armed Forces')),
            (0, _(u'00 - Economically inactive'))
        )
        super(OccupationField, self).__init__(*args, **kwargs)


class ReligionField(models.PositiveSmallIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = (
            (1, _(u'01 - Buddhist')),
            (2, _(u'02 - Islam')),
            (3, _(u'03 - Christian')),
            (4, _(u'04 - Hindu')),
            (5, _(u'05 - Animist')),
            (6, _(u'06 - Confucian')),
            (7, _(u'07 - Sikh')),
            (8, _(u'08 - Jew')),
            (9, _(u'09 - Others')),
            (10, _(u'Not stated'))
        )
        super(ReligionField, self).__init__(*args, **kwargs)


class OriginalFormField(models.ImageField):
    def __init__(self, *args, **kwargs):
        kwargs['upload_to'] = make_image_path
        kwargs['verbose_name'] = _(u"Original form image")
        kwargs['help_text'] = _(u'Please attach a scanned copy of a photograph on the original form')
        super(OriginalFormField, self).__init__(*args, **kwargs)


class CitizenshipField(models.PositiveSmallIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = (
            (1, _(u'01 - Myanmar')),
            (2, _(u'02 - Indian')),
            (3, _(u'03 - Pakistani')),
            (4, _(u'04 - Bangladesh')),
            (5, _(u'05 - Nepalese')),
            (6, _(u'06 - Chinese')),
            (7, _(u'07 - European/American')),
            (8, _(u'08 - Other Asian')),
            (9, _(u'09 - Others')),
            (10, _(u'10 - Not stated')),
        )
        super(CitizenshipField, self).__init__(*args, **kwargs)


class Char300Field(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 300
        super(Char300Field, self).__init__(*args, **kwargs)


class Char100Field(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 100
        super(Char100Field, self).__init__(*args, **kwargs)


class ExtraOccupationField(models.CharField):
    """
    issue #621
    """

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 100
        kwargs['verbose_name'] = _(u'Occupation (optional description)')

        super(ExtraOccupationField, self).__init__(*args, **kwargs)
