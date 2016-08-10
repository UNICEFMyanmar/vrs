# -*- coding: utf-8 -*-
import datetime

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_init
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _, string_concat
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from report_builder.models import DisplayField

from .fields import get_township, Char100Field, OriginalFormField, CitizenshipField, ReligionField, \
    RaceField, OccupationField, StateDivisionField, DistrictField, TownshipField, Char300Field, SerialNoField, \
    AreaField, PlaceField, CIRfield, AGEfield, E_CODEField, CERTField, SEXField, ExtraOccupationField, N_CODEField, \
    AgeGroupField
from .codes import YANGON_HOSPITAL_NOT_MENTIONED_CODE, YANGON_STATE_DIVISION_CODE, \
    ANY_HOSPITAL_CODE, \
    Sub_code_No_Dictionary, \
    validate_location_codes, URBAN, RURAL, BORN_ALIVE, BORN_DEAD, \
    PRE_DELI_YES, PRE_DELI_NO, SEX_MALE, SEX_FEMALE, CODE_DELIMITER
from .permissions import get_user_Q_s

DATE_HELP_TEXT = _(u'Day, month and year: <kbd>25102006</kbd>')


class FormManager(models.Manager):
    def get_queryset_for_user(self, user, **kwargs):
        form_name = self.model._meta.model_name
        Qs = get_user_Q_s(user, form_name)

        if Qs:
            return super(FormManager, self).get_queryset(**kwargs).filter(Qs)
        else:
            return super(FormManager, self).get_queryset(**kwargs).none()


class HospitalManager(models.Manager):
    def _as_choices(self, qs):

        choices = [('', '---------')]
        twn = 0
        RHCs = []

        for rhc in qs:
            if not twn:
                twn = rhc.TWN
            if not rhc.TWN == twn:
                choices.append((get_township(twn), RHCs))
                RHCs = []
                twn = rhc.TWN
            RHCs.append([rhc.pk, rhc])
        if RHCs:
            choices.append((get_township(twn), RHCs))

        choices.append(('99', _('99 - Not stated')))
        return choices

    def birth_as_choices(self):
        model = self.model
        return self._as_choices(model.objects.filter(birth=True))

    def death_as_choices(self):
        model = self.model
        return self._as_choices(model.objects.filter(death=True))


class RHCManager(models.Manager):
    def as_choices(self):
        model = self.model
        choices = [('', '---------')]
        twn = 0
        RHCs = []
        for rhc in model.objects.all().order_by('TWN'):
            if not twn:
                twn = rhc.TWN
            if not rhc.TWN == twn:
                choices.append((get_township(twn), RHCs))
                RHCs = []
                twn = rhc.TWN
            RHCs.append([rhc.pk, rhc])

        if twn and RHCs:
            choices.append((get_township(twn), RHCs))

        return choices


class Hospital(models.Model):
    class Meta:
        app_label = "birth_registration"
        verbose_name = _(u'Hospital')
        verbose_name_plural = _(u"Hospitals")
        unique_together = ('ST_DV', 'DIS', 'TWN', 'code')

    objects = HospitalManager()

    ST_DV = StateDivisionField(blank=False)

    DIS = DistrictField(blank=False)

    TWN = TownshipField(blank=False)

    code = models.PositiveSmallIntegerField(
        _(u'Code'),
        blank=False,
        unique=True
    )

    name = models.CharField(
        _(u'Name'),
        blank=False,
        max_length=100
    )

    birth = models.BooleanField(_(u'Birth registration'), blank=True)
    death = models.BooleanField(_(u'Death registration'), blank=True)

    def __unicode__(self):
        return "%02d - %s" % (self.code, self.name)

    def clean(self):
        validation_errors = validate_location_codes(
            self.ST_DV, 'ST_DV',
            self.DIS, 'DIS',
            self.TWN, 'TWN'
        )

        if len(validation_errors):
            raise ValidationError(validation_errors)


class RHC(models.Model):
    class Meta:
        app_label = "birth_registration"
        verbose_name = _(u'RHC')
        verbose_name_plural = _(u"RHCs")
        unique_together = ('ST_DV', 'DIS', 'TWN', 'RHC')

    objects = RHCManager()

    ST_DV = StateDivisionField(blank=False)

    DIS = DistrictField(blank=False)

    TWN = TownshipField(blank=False)

    RHC = models.PositiveSmallIntegerField(
        _(u'RHC Code'),
        blank=False,
    )

    Village = models.CharField(
        _(u'Village'),
        blank=False,
        max_length=100
    )

    def __unicode__(self):
        return "%02d - %s" % (self.RHC, self.Village)

    def clean(self):
        validation_errors = validate_location_codes(
            self.ST_DV, 'ST_DV',
            self.DIS, 'DIS',
            self.TWN, 'TWN'
        )

        if len(validation_errors):
            raise ValidationError(validation_errors)


class RHCfield(models.ForeignKey):
    def __init__(self, *args, **kwargs):
        kwargs['to'] = RHC
        kwargs['help_text'] = _(u'RHC code (rural areas)')

        super(RHCfield, self).__init__(*args, **kwargs)


DO_NOT_UPDATE_UPDATE_AT = 'DO_NOT_UPDATE_UPDATE_AT'


class UpdateUpdatedAt(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if DO_NOT_UPDATE_UPDATE_AT not in kwargs:
            if hasattr(self, 'updated_at'):
                self.updated_at = datetime.datetime.now()
        else:
            kwargs.pop(DO_NOT_UPDATE_UPDATE_AT)
        super(UpdateUpdatedAt, self).save(*args, **kwargs)

    def validate_RHC_CIR(self):
        validation_errors = {}

        for field in self._meta.get_fields():
            if type(field) == AreaField:
                area_field_value = getattr(self, field.name)
                break
        else:
            raise NotImplementedError('Area field is not found')

        for field in self._meta.get_fields():
            if type(field) == StateDivisionField:
                state_division_field_value = getattr(self, field.name)
                break
        else:
            raise NotImplementedError('State division field is not found')

        for field in self._meta.get_fields():
            if type(field) == TownshipField:
                twn_field_value = getattr(self, field.name)
                break
        else:
            raise NotImplementedError('Township field is not found')

        if area_field_value == URBAN:
            if self.RHC:
                validation_errors['RHC'] = [_(u'You can not use this field for urban areas'), ]

            if self.CIR:
                if state_division_field_value == YANGON_STATE_DIVISION_CODE:
                    if not (
                                (self.CIR in Sub_code_No_Dictionary.get(twn_field_value, []))
                            or
                                (self.CIR == YANGON_HOSPITAL_NOT_MENTIONED_CODE)
                    ):
                        validation_errors['CIR'] = [_(u'This hospital belongs to another township or town'), ]

                elif self.CIR != ANY_HOSPITAL_CODE:
                    validation_errors['CIR'] = [
                        _(u'Please check the code: looks like it should be %s') % ANY_HOSPITAL_CODE, ]

        elif area_field_value == RURAL:
            if self.CIR and self.CIR != ANY_HOSPITAL_CODE:
                validation_errors['CIR'] = [
                    _(u'Please check the code: looks like it should be %s') % ANY_HOSPITAL_CODE, ]

            if not self.RHC:
                validation_errors['RHC'] = [_(u'This field is required for rural areas'), ]
            else:
                rhc = RHC.objects.get(pk=self.RHC_id)
                if rhc.TWN != twn_field_value:
                    validation_errors['RHC'] = [_(u'This RHC belongs to another township'), ]

        return validation_errors

    def validate_hospitals(self):

        validation_errors = {}

        for field in self._meta.get_fields():
            if type(field) == TownshipField:
                twn_field_value = getattr(self, field.name)
                break
        else:
            raise NotImplementedError('Township field is not found')

        if self.Hospital:
            if not (
                        (self.Hospital.TWN == twn_field_value)
                    or
                        (self.Hospital == YANGON_HOSPITAL_NOT_MENTIONED_CODE)
            ):
                validation_errors['Hospital'] = [_(u'This hospital belongs to another township or town'), ]

        if len(filter(None, [self.Hospital, self.governmental_hospital, self.private_hospital])) > 1:
            if self.Hospital:
                validation_errors['Hospital'] = [_(u'Conflicting value'), ]
            if self.governmental_hospital:
                validation_errors['governmental_hospital'] = [_(u'Conflicting value'), ]
            if self.private_hospital:
                validation_errors['private_hospital'] = [_(u'Conflicting value'), ]

        return validation_errors


class F101(UpdateUpdatedAt):
    class Meta:
        verbose_name = _(u"Form 101")
        verbose_name_plural = _(u"Forms 101")

    objects = FormManager()

    ST_DV = StateDivisionField(_(u"State/Division"), blank=False)

    DIS = DistrictField(_(u"District"), blank=False)

    TWN = TownshipField(_(u"Township or town"), blank=False)

    NR_AREA = AreaField(_(u"Area"), blank=False)

    CIR = CIRfield(blank=True, null=True)

    RHC = RHCfield(
        blank=True,
        null=True,
    )

    Hospital = models.ForeignKey(Hospital, blank=True, null=True)
    governmental_hospital = Char100Field(_('Governmental hospital name'), blank=True, null=True)
    private_hospital = Char100Field(_('Private hospital name'), blank=True, null=True)

    NR_SNO = SerialNoField(blank=False)

    Date_of_Registration = models.DateField(
        _(u'Date of Registration'),
        help_text=DATE_HELP_TEXT,
        blank=False,
        # default=datetime.datetime.now()
    )

    NRYY = models.PositiveSmallIntegerField(
        _(u'Date of Registration - year'),
        blank=True
    )

    NRMM = models.PositiveSmallIntegerField(
        _(u'Date of Registration - month'),
        blank=True
    )

    # ################################################################################

    NBTH = models.PositiveSmallIntegerField(
        _(u'Birth status'),
        blank=False,
        help_text=_(u'<ul><li>'
                    u'Born alive = 1 '
                    u'</li><li>'
                    u'Born dead = 2'
                    u'</li></ul>'),
        choices=(
            (BORN_ALIVE, _(u'01 - Born alive')),
            (BORN_DEAD, _(u'02 - Born dead'))
        )
    )

    NBTH_comment = Char300Field(
        _(u"Optional comment"),
        blank=True,
        null=True
    )

    Date_of_Birth = models.DateField(
        _(u'Date of Birth'),
        help_text=DATE_HELP_TEXT,
        blank=False,
    )

    NDYY = models.PositiveSmallIntegerField(
        _(u'Date of Birth - year'),
        blank=True
    )

    NDMM = models.PositiveSmallIntegerField(
        _(u'Date of Birth - month'),
        blank=True
    )

    NPLACE_B = PlaceField(_(u"Place of Birth"),
                          help_text=_(u"Check if place of birth given in entry form (may be residence). "
                                      u"Enter area of Yangon only if a house address. "
                                      u"If a hospital or nursing home etc. give full address.<br/>"
                                      u"<ul><li>"
                                      u"Home/House = 1"
                                      u"</li>"
                                      u"<li>"
                                      u"Government Hospital = 2"
                                      u"</li>"
                                      u"<li>"
                                      u"Nursing Home (including any maternity and child welfare society) = 3"
                                      u"</li>"
                                      u"<li>"
                                      u"Private Hospital/clinic = 4"
                                      u"</li>"
                                      u"<li>"
                                      u"Other institution = 5"
                                      u"</li>"
                                      u"<li>"
                                      u"Elsewhere = 6"
                                      u"</li></ul>"),
                          blank=False
                          )

    Name_of_child = Char100Field(
        _(u'Name of child'),
        help_text=_(u'(if has)'),
        blank=True,
        null=True,
    )

    NSEX = models.PositiveSmallIntegerField(
        _(u"Sex"),
        choices=(
            (1, _(u'01 - Male')),
            (2, _(u'02 - Female'))
        ),
        help_text=_(u'<ul><li>Male = 1 </li><li>Female = 2 </li></ul>'),
        blank=False
    )

    # #################################################################

    Father_name = Char100Field(
        _(u"Father's name"),
        blank=True,
        null=True
    )

    NRACE_F = RaceField(_(u"Father's race"), blank=True, null=True)

    Father_NRC = Char100Field(
        _(u"Father's NRC"),
        blank=True,
        null=True
    )

    NCZN_F = CitizenshipField(_(u"Father's citizenship"), blank=True, null=True)

    NREL_F = ReligionField(_(u"Father's Religion"), blank=True, null=True)

    NOCC_F = OccupationField(_(u"Father's occupation"), blank=True, null=True)

    # issue #621
    Occupation_F = ExtraOccupationField(blank=True)

    # ######################################################################

    Mother_name = Char100Field(_(u"Mother's name"), blank=False, null=True)

    NRACE_M = RaceField(_(u"Mother's race"), blank=True, null=True)

    Mother_NRC = Char100Field(
        _(u"Mother's NRC"),
        blank=True,
        null=True
    )

    NCZN_M = CitizenshipField(_(u'Mother\'s citizenship'), blank=True, null=True)

    NREL_M = ReligionField(_(u"Mother's Religion"), blank=True, null=True)

    NOCC_M = OccupationField(_(u"Mother's occupation"), blank=True, null=True)

    # issue #621
    Occupation_M = ExtraOccupationField(blank=True)

    RST_DV = StateDivisionField(_(u'Usual Place of residence of mother:'), help_text=_(u' State Division'), blank=True,
                                null=True)

    RDIS = DistrictField(_(u'Usual Place of residence of mother:'), help_text=_(u'District'), blank=True, null=True)

    RTWN = TownshipField(_(u'Usual Place of residence of mother:'), help_text=_(u'Township or town'), blank=True,
                         null=True)

    RCIR = Char300Field(_(u"Address of mother"), blank=True, null=True)

    # ######################################################################

    Informer = Char300Field(
        _(u"Informer's name, address and relation to the child:"),
        blank=True,
        null=True,
    )

    # ######################################################################
    # ######################################################################

    NTYPE_B = models.PositiveSmallIntegerField(
        _(u'Type of birth'),
        choices=(
            (1, _(u'01 - Single')),
            (2, _(u'02 - Twins')),
            (3, _(u'03 - Triplets')),
            (4, _(u'04 - Quadruplets and above')),
        ),
        help_text=_(u'<ul><li>'
                    u'Single = 1'
                    u'</li><li>'
                    u'Twins = 2'
                    u'</li><li>'
                    u'Triplets = 3'
                    u'</li><li>'
                    u'Quadruplets and above = 4'
                    u'</li></ul>'
                    ),
        blank=True,
        null=True
    )

    NMULTI_B_CHOICES = (
        (
            _(u'For both alive'),
            (
                (1, _(u'01 - 2 Females')),
                (2, _(u'02 - 1 Male and 1 Female')),
                (3, _(u'03 - 2 Males'))
            )
        ),
        (
            _(u'For 1 alive'),
            (
                (4, _(u'04 - 2 females')),
                (5, _(u'05 - 1 live male')),
                (6, _(u'06 - 1 live female')),
                (7, _(u'07 - 2 males'))
            )
        ),
        (
            _(u'For born dead'),
            (
                (8, _(u'08 - 2 females')),
                (9, _(u'09 - 1 Male and 1 Female')),
                (10, _(u'10 - 2 Males'))
            )
        ),
        (
            _(u'For 3 born alive'), (
                (11, _(u'11 - 3 Females')),
                (12, _(u'12 - 1 Male')),
                (13, _(u'13 - 2 Males')),
                (14, _(u'14 - 3 Males'))
            )
        ),
        (
            _(u'For 2 born alive & 1 born dead'),
            (
                (15, _(u'15 - 2 LF & 1 SM')),
                (16, _(u'16 - 2 LF & 1 SF')),
                (17, _(u'17 - 2 LM & 1 SM')),
                (18, _(u'18 - 2 LM & 1 SF')),
                (19, _(u'19 - 1 LM & 1 LF, 1 SM')),
                (20, _(u'20 - 1 LM & 1 LF, 1 SF')),
            )
        ),
        (
            _(u'For 1 born alive & 2 born dead'),
            (
                (21, _(u'21 - 1 LF & 2 SM')),
                (22, _(u'22 - 1 LF & 2 SF')),
                (23, _(u'23 - 1 LM& 2 SM')),
                (24, _(u'24 - 1 LM & 2 SF')),
                (25, _(u'25 - 1 LF, 1 SM & 1 SF')),
                (26, _(u'26 - 1 LM, 1 SM & 1 SF'))
            ),
        ),
        (
            _(u'For all born dead'),
            (
                (27, _(u'27 - 3 Females')),
                (28, _(u'28 - 1 Male')),
                (29, _(u'29 - 2 Males')),
                (30, _(u'30 - 3 Males'))
            )
        ),
    )

    NTYPE_B_validation = {
        2: (1, 10),
        3: (11, 30)
    }

    NMULTI_B = models.PositiveSmallIntegerField(
        _(u'Twins'),
        choices=NMULTI_B_CHOICES,
        blank=True,
        null=True
    )

    NATT_B = models.PositiveSmallIntegerField(
        _(u'Attendant at birth'),
        choices=(
            (1, _(u'01 - Doctor')),
            (2, _(u'02 - Registered midwife or nurse')),
            (3, _(u'03 - Auxiliary midwife')),
            (4, _(u'04 - Lethe (Trained Traditional Birth Attendant) TTBA')),
            (5, _(u'05 - Other')),
        ),
        blank=True,
        null=True
    )

    NAGE_M = models.PositiveSmallIntegerField(
        _(u'Age of Mother'),
        help_text=_(u'Enter age, unknown age = 99'),
        validators=[MaxValueValidator(99)],
        blank=True,
        null=True
    )

    NAGP_M_VALUES = (
        (0, (00, 14)),
        (1, (15, 19)),
        (2, (20, 24)),
        (3, (25, 29)),
        (4, (30, 34)),
        (5, (35, 39)),
        (6, (40, 44)),
        (7, (45, 49)),
        (8, (50, 98)),
        (9, (99, 100))
    )

    NAGP_M = models.PositiveSmallIntegerField(
        _(u'Age of Mother - code'),
        help_text=_(u'Enter age as shown in information form on left hand side of word AGE for 1st two columns '
                    u'and then code as shown for the 3rd column'),
        choices=(
            (0, _(u'00 - Under 15 Years')),
            (1, _(u'01 - 15 – 19')),
            (2, _(u'02 - 20 – 24')),
            (3, _(u'03 - 25 – 29')),
            (4, _(u'04 - 30 – 34')),
            (5, _(u'05 - 35 – 39')),
            (6, _(u'06 - 40 – 44')),
            (7, _(u'07 - 45 – 49')),
            (8, _(u'08 - 50 and over')),
            (9, _(u'09 - Unknown age (99)')),
        ),
        blank=True,
        null=True
    )

    WEIGHT = models.PositiveSmallIntegerField(
        _(u'Weight of baby at birth'),
        help_text=_(u'Code 4 digits in gram. If weight of baby is shown in pound use conversion table'),
        validators=[
            MaxValueValidator(9999),
        ],
        blank=True,
        null=True,

    )

    PERIOD = models.PositiveSmallIntegerField(
        _(u'Gestational period'),
        help_text=_(u'Code 2 digits in week'),
        validators=[
            MaxValueValidator(99),
        ],
        blank=True,
        null=True,
    )

    NUMBER_OF_CHILDREN_HELP_TEXT = _(u'99 - Not Stated')

    NPRV_CH = models.PositiveSmallIntegerField(
        _(u"Mother\'s previous children (Excluding this one)"),
        help_text=NUMBER_OF_CHILDREN_HELP_TEXT,
        validators=[
            MaxValueValidator(99),
        ],
        blank=True,
        null=True,
    )

    NB_ALIV = models.PositiveSmallIntegerField(
        _(u'Number born alive (Excluding this one)'),
        help_text=NUMBER_OF_CHILDREN_HELP_TEXT,
        blank=True,
        null=True
    )

    Original_form = OriginalFormField(upload_to='F101/%Y/%m/%d/', blank=True, null=True)

    NOPR = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(editable=False)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.pk)

    def clean(self):
        validation_errors = validate_location_codes(
            self.ST_DV, 'ST_DV',
            self.DIS, 'DIS',
            self.TWN, 'TWN'
        )

        validation_errors.update(self.validate_RHC_CIR())

        if self.RST_DV and self.RDIS and self.RTWN:  # validate Mother's residence location
            validation_errors.update(
                validate_location_codes(
                    self.RST_DV, 'RST_DV',
                    self.RDIS, 'RDIS',
                    self.RTWN, 'RTWN'
                )
            )

        if self.NB_ALIV > self.NPRV_CH:  # number of children
            validation_errors['NB_ALIV'] = [
                _(u'Please check the code')]

        if self.Date_of_Birth:
            if self.Date_of_Birth > datetime.date.today():
                validation_errors['Date_of_Birth'] = [_('The date cannot be in the future')]

        if self.Date_of_Registration:
            if self.Date_of_Registration > datetime.date.today():
                validation_errors['Date_of_Registration'] = [_('The date cannot be in the future')]

        if self.Date_of_Birth and self.Date_of_Registration:
            if self.Date_of_Registration < self.Date_of_Birth:
                validation_errors['Date_of_Registration'] = [
                    _('Date of registration can not be before the date of birth')]

        if self.NTYPE_B == 1 and self.NMULTI_B:
            validation_errors['NTYPE_B'] = [
                _('Wrong type of birth?')]

        if self.NTYPE_B in self.NTYPE_B_validation.keys():
            (NMULTI_B_min, NMULTI_B_max) = self.NTYPE_B_validation[self.NTYPE_B]

            if not (self.NMULTI_B <= NMULTI_B_max and self.NMULTI_B >= NMULTI_B_min):
                validation_errors['NMULTI_B'] = [
                    _('Please check the value (should be %d to %d)' % (NMULTI_B_min, NMULTI_B_max))]

        validation_errors.update(self.validate_hospitals())

        if validation_errors:
            raise ValidationError(validation_errors)

    def save(self, *args, **kwargs):
        if self.NAGE_M:
            for key, val in self.NAGP_M_VALUES:
                if val[0] <= self.NAGE_M <= val[1]:
                    self.NAGP_M = key
                    break

        if self.Date_of_Registration:
            self.NRYY = self.Date_of_Registration.year
            self.NRMM = self.Date_of_Registration.month

        if self.Date_of_Birth:
            self.NDYY = self.Date_of_Birth.year
            self.NDMM = self.Date_of_Birth.month

        if self.NMULTI_B == u'':
            self.NMULTI_B = None

        super(F101, self).save(*args, **kwargs)


class F201(UpdateUpdatedAt):
    class Meta:
        verbose_name = _("Form 201")
        verbose_name_plural = _("Forms 201")

    objects = FormManager()

    NNRT = StateDivisionField(_(u"State/Division"), blank=False)

    NNRT1 = DistrictField(_(u"District"), blank=False)

    NNST = TownshipField(_(u"Township or town"), blank=False)

    NNVD = AreaField(
        _(u"Area"),
    )

    CIR = CIRfield(
        blank=True,
        null=True,
    )

    RHC = RHCfield(
        blank=True,
        null=True,
    )

    Hospital = models.ForeignKey(Hospital, blank=True, null=True)
    governmental_hospital = Char100Field(_('Governmental hospital name'), blank=True, null=True)
    private_hospital = Char100Field(_('Private hospital name'), blank=True, null=True)

    SNER = SerialNoField(blank=False)

    Date_of_Registration = models.DateField(
        _(u"Date of Registration"),
        help_text=DATE_HELP_TEXT,
        blank=False,
        # default=datetime.datetime.now()
    )

    DRY = models.PositiveSmallIntegerField(
        _(u'Date of Registration - year'),
        blank=True,
        validators=[MinValueValidator(1900), MaxValueValidator(2100)]
    )

    DRM = models.PositiveSmallIntegerField(
        _(u'Date of Registration - month'),
        blank=True,
        validators=[MaxValueValidator(12)]
    )

    Date_of_Death = models.DateField(
        _(u'Date of Death'),
        help_text=DATE_HELP_TEXT,
        blank=False,
    )

    DDY = models.PositiveSmallIntegerField(
        _(u'Date of Death - year'),
        blank=True,
        validators=[MinValueValidator(1900), MaxValueValidator(2100)]
    )

    DDM = models.PositiveSmallIntegerField(
        _(u'Date of Death - month'),
        blank=True,
        validators=[MaxValueValidator(12)]
    )

    PLD = PlaceField(_(u"Place of Death"),
                     help_text=_(u"Check if place of death given in entry form (may be residence).<br/>"
                                 u"Enter area of Yangon only if a house address.<br/>"
                                 u"If a hospital or nursing home etc. give full address."), blank=False)

    Name = Char100Field(_(u"Name"), blank=False, null=True)

    SEX = SEXField(
        blank=False
    )

    #    AGE = AGEfield(blank=False)
    #    AGE_CODE = models.SmallIntegerField(_(u"Age code"), blank=True, null=True)
    AGE_GROUP = AgeGroupField(_(u'Age Group'), default=99, blank=False)

    EXTRA_AGE_CODE_1_1 = '1-1'
    EXTRA_AGE_CODE_2_3 = '2-3'
    EXTRA_AGE_CODE_3_2 = '3-2'
    EXTRA_AGE_CODE_3_3 = '3-3'

    EXTRA_AGE_CODE_CHOICES = (
        (EXTRA_AGE_CODE_1_1, _(u'1-1')),
        (EXTRA_AGE_CODE_2_3, _(u'2-3')),
        (EXTRA_AGE_CODE_3_2, _(u'3-2')),
        (EXTRA_AGE_CODE_3_3, _(u'3-3')),
    )

    EXTRA_AGE_CODE = models.CharField(
        _(u"Extra age code"), max_length=3, choices=EXTRA_AGE_CODE_CHOICES, blank=True, null=True
    )  # issue #620

    OCCU = OccupationField(_(u"Occupation"), blank=True)

    # issue #621
    Occupation = ExtraOccupationField(blank=True)

    RACE = RaceField(_(u"Race"), blank=True)

    CTIZ = CitizenshipField(_(u"Citizenship"), blank=True)

    NRC = Char100Field(
        _(u"NRC"),
        blank=False,
        null=True
    )

    REL = ReligionField(_(u"Religion"), blank=True)

    UPRS = StateDivisionField(_(u"Usual place of residence"), help_text=_(u" State Division"), blank=True, null=True)

    UPRS1 = DistrictField(_(u"Usual place of residence"), help_text=_(u"District"), blank=True, null=True)

    UPCR = TownshipField(_(u"Usual place of residence"), help_text=_(u'Township or town'), blank=True, null=True)

    RCIR = Char300Field(_(u"Usual place of residence"), blank=True, null=True)

    # according to test.xls
    E_CODE = E_CODEField(_("E-Code"), blank=True, null=True)
    # according to test.xls
    N_CODE = N_CODEField(_("N-Code"), blank=False, null=True)

    Father_name = Char100Field(_(u"Father's name"), blank=False, null=True)

    Mother_name = Char100Field(_(u"Mother's name"), blank=True, null=True)

    Informant_name = models.CharField(
        _(u"Informant's name, address and relationship to deceased"),
        blank=True,
        null=True,
        max_length=300
    )

    MRIT = models.PositiveSmallIntegerField(
        _(u"Marital status of deceased"),
        choices=(
            (1, _(u'01 - Never married (Single)')),
            (2, _(u'02 - Married')),
            (3, _(u'03 - Divorced')),
            (4, _(u'04 - Separated')),
            (5, _(u'05 - Widowed')),
            (6, _(u'06 - Renounced')),
            (7, _(u'07 - Not stated')),
        ),
        blank=True,
        null=True,
    )

    PRE = models.PositiveSmallIntegerField(
        _(u'If a woman was the death associated with pregnancy'),
        choices=(
            (PRE_DELI_YES, _(u'01 - Yes')),
            (PRE_DELI_NO, _(u'02 - No')),
        ),
        blank=True,
        null=True
    )

    DELI = models.PositiveSmallIntegerField(
        _(u'Was there a delivery'),
        choices=(
            (PRE_DELI_YES, _(u'01 - Yes')),
            (PRE_DELI_NO, _(u'02 - No')),
        ),
        blank=True,
        null=True
    )

    CERT = CERTField(
        blank=True,
        null=True
    )

    Original_form = OriginalFormField(blank=True, null=True)

    OPR = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(editable=False)
    deleted = models.BooleanField(default=False)

    # @property
    # def age_years(self):
    #
    #     if not self.AGE.isdigit():
    #         return 99
    #     else:
    #         age = int(self.AGE)
    #
    #     if age > 199:
    #         return 1
    #     elif age == 199:
    #         return 99
    #     else:
    #         return age

    # @staticmethod
    # def age_code(age):
    #     if age.isdigit() and age != "900":
    #         age = int(age)
    #     else:
    #         return 99
    #
    #     if age < 5:
    #         return age
    #     elif age < 85:
    #         return age // 5 + 4
    #     elif age < 200:
    #         return 21
    #     else:
    #         return 0

    def extra_age_code(self):
        if self.SEX != SEX_FEMALE:
            return ""

        # todo: fix!
        if self.AGE_GROUP >= 15 or self.AGE_GROUP <= 7:  # age >= 50 or age <= 14:
            return F201.EXTRA_AGE_CODE_1_1
        elif self.PRE != PRE_DELI_YES:
            return F201.EXTRA_AGE_CODE_3_3
        elif self.PRE != PRE_DELI_NO:
            if self.DELI == PRE_DELI_YES:
                return F201.EXTRA_AGE_CODE_3_2
            elif self.DELI == PRE_DELI_NO:
                return F201.EXTRA_AGE_CODE_2_3

        return ""

    def __unicode__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        if self.Date_of_Registration:
            self.DRY = self.Date_of_Registration.year
            self.DRM = self.Date_of_Registration.month

        if self.Date_of_Death:
            self.DDY = self.Date_of_Death.year
            self.DDM = self.Date_of_Death.month

        # self.AGE_CODE = self.age_code(self.AGE)
        self.EXTRA_AGE_CODE = self.extra_age_code()

        super(F201, self).save(*args, **kwargs)

    def clean(self):
        validation_errors = validate_location_codes(
            self.NNRT, 'NNRT',
            self.NNRT1, 'NNRT1',
            self.NNST, 'NNST'
        )

        validation_errors.update(self.validate_RHC_CIR())

        if self.UPRS and self.UPRS1 and self.UPCR:  # validate usual residence location
            validation_errors.update(
                validate_location_codes(
                    self.UPRS, 'UPRS',
                    self.UPRS1, 'UPRS1',
                    self.UPCR, 'UPCR'
                )
            )

        # todo: test me!
        if self.SEX == SEX_MALE and self.DELI == PRE_DELI_YES:
            validation_errors['DELI'] = [_(
                'Please check this field value or "%s" field value above' %
                self._meta.get_field_by_name('SEX')[0].verbose_name)]

        if self.SEX == SEX_MALE and self.PRE == PRE_DELI_YES:
            validation_errors['PRE'] = [_(
                'Please check this field value or "%s" field value above' %
                self._meta.get_field_by_name('SEX')[0].verbose_name)]

        if self.Date_of_Death:
            if self.Date_of_Death > datetime.date.today():
                validation_errors['Date_of_Death'] = [_('The date cannot be in the future')]

        if self.Date_of_Registration:
            if self.Date_of_Registration > datetime.date.today():
                validation_errors['Date_of_Registration'] = [_('The date cannot be in the future')]

        if self.Date_of_Death and self.Date_of_Registration:
            if self.Date_of_Registration < self.Date_of_Death:
                validation_errors['Date_of_Registration'] = [
                    _('Date of registration can not be before the date of death')]

        if len(validation_errors):
            raise ValidationError(validation_errors)


# remove choice from Django Reports Fields - kind of a dirty hack, sorry
@receiver(pre_init, sender=DisplayField)
def remove_choices_from_report_fields(sender, **kwargs):
    def get_choices(self, model, field_name):
        if self.aggregate != "Max":
            print "<", self.aggregate, ">"
            return []
        else:
            try:
                model_field = model._meta.get_field_by_name(field_name)[0]
            except:
                model_field = None
            if model_field and model_field.choices:
                return ((model_field.get_prep_value(key), val) for key, val in model_field.choices)

    sender.get_choices = get_choices


class Profile(models.Model):
    class Meta:
        verbose_name = _(u"Authority")
        verbose_name_plural = _(u"Authority")

    authority = models.CharField(
        _(u'Authority'),
        max_length=100,
        blank=True,
        null=True,
    )

    position = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=_(
        u"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    phone = models.CharField(validators=[phone_regex], blank=True, null=True, max_length=16)
    NOPR = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, editable=False)


def validate_2digits(value):
    if not isinstance(value, int) or not (0 < value < 100):
        raise ValidationError(_(u'%d should be two digits integer') % value)
