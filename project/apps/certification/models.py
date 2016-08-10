# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from birth_registration.fields import TownshipField, StateDivisionField, SerialNoField, Char100Field, RaceField, \
    CitizenshipField, ReligionField, OccupationField, PlaceField, AreaField, CIRfield, \
    AGEfield, E_CODEField, CERTField, SEXField, Char300Field, ExtraOccupationField, AgeGroupField
from birth_registration.fields import DistrictField
from birth_registration.models import F101, FormManager, RHC, DATE_HELP_TEXT, UpdateUpdatedAt, RHCfield, F201, Hospital


class Certificate(UpdateUpdatedAt):
    class Meta:
        app_label = 'certification'
        abstract = True


class F103(Certificate):
    class Meta:
        app_label = 'certification'
        verbose_name = _("Form 103")
        verbose_name_plural = _("Forms 103")

    f101 = models.ForeignKey(F101)

    objects = FormManager()

    ST_DV = StateDivisionField(_(u"State/Division"), blank=False)

    DIS = DistrictField(_(u"District"), blank=False)

    TWN = TownshipField(_(u"Township or town"), blank=False)

    NR_AREA = AreaField(_(u"Area"), blank=False)

    CIR = CIRfield(
        blank=True,
        null=True
    )

    RHC = RHCfield(
        blank=True,
        null=True,
    )

    Hospital = models.ForeignKey(Hospital, blank=True, null=True)
    governmental_hospital = Char100Field(_('Governmental hospital name'), blank=True, null=True)
    private_hospital = Char100Field(_('Private hospital name'), blank=True, null=True)

    Date_of_Registration = models.DateField(
        _(u'Date of Registration'),
        blank=False,
    )

    NR_SNO = SerialNoField(blank=False)

    Date_of_Birth = models.DateField(
        _(u'Date of Birth'),
        blank=False,
    )

    Name_of_child = Char100Field(
        _(u'Name of child'),
        blank=False,
        null=False,
    )

    NSEX = models.PositiveSmallIntegerField(
        _(u"Sex"),
        choices=(
            (1, _(u'01 - Male')),
            (2, _(u'02 - Female'))
        ),
        blank=False
    )

    NPLACE_B = PlaceField(_(u"Place of Birth"))

    # #################################################################

    Father_name = Char100Field(_(u"Father's Name"), blank=True, null=True)

    NRACE_F = RaceField(_(u"Father's Race"), blank=True, null=True)

    NCZN_F = CitizenshipField(_(u"Father's Citizenship"), blank=True, null=True)

    NREL_F = ReligionField(_(u"Father's Religion"), blank=True, null=True)

    NOCC_F = OccupationField(_(u"Father's Occupation"), blank=True, null=True)

    # issue #621
    Occupation_F = ExtraOccupationField(blank=True, null=True)

    # ######################################################################

    Mother_name = Char100Field(_(u"Mother's Name"), blank=False, null=True)

    NCZN_M = CitizenshipField(_(u'Mother\'s citizenship:'), blank=True, null=True)

    NRACE_M = RaceField(_(u"Mother's Race"), blank=True, null=True)

    NREL_M = ReligionField(_(u"Mother's Religion"), blank=True, null=True)

    NOCC_M = OccupationField(_(u"Mother's occupation"), blank=True, null=True)

    # issue #621
    Occupation_M = ExtraOccupationField(blank=True, null=True)

    RCIR = models.TextField(_(u"Mother's Address"), blank=True, null=True)

    ######################################################################

    Informer = models.TextField(
        _(u"Informer's name and address"),
        blank=True,
        null=True,
    )

    NOPR = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'Registration Officer'), null=True,
                             editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return str(self.pk)


class F203(Certificate):
    class Meta:
        verbose_name = _("Form 203")
        verbose_name_plural = _("Forms 203")

    f201 = models.ForeignKey(F201)

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
        _(u"Date of registration"),
        help_text=DATE_HELP_TEXT,
        blank=False,
        # default=datetime.datetime.now()
    )

    Date_of_Death = models.DateField(
        _(u'Date of Death'),
        help_text=DATE_HELP_TEXT,
        blank=False,
    )

    PLD = PlaceField(_(u"Place of Death"),
                     help_text=_(u"Check if place of death given in entry form (may be residence).<br/>"
                                 u"Enter area of Yangon only if a house address.<br/>"
                                 u"If a hospital or nursing home etc. give full address."))

    Name = Char100Field(_(u"Name"), blank=True, null=True)

    SEX = SEXField(
        blank=False
    )

    AGE_GROUP = AgeGroupField(_(u'Age Group'), default=99, blank=False)

    OCCU = OccupationField(_(u"Occupation"), blank=True)

    # issue #621
    Occupation = ExtraOccupationField(blank=True)

    RACE = RaceField(_(u"Race"), blank=True)

    CTIZ = CitizenshipField(_(u"Citizenship"), blank=True)

    REL = ReligionField(_(u"Religion"), blank=True)

    UPRS = StateDivisionField(_(u"State/Division"), help_text=_(u"Usual place of residence"), blank=True, null=True)

    UPRS1 = DistrictField(_(u"District"), help_text=_(u"Usual place of residence"), blank=True, null=True)

    UPCR = TownshipField(_(u"Township"), help_text=_(u"Usual place of residence"), blank=True, null=True)

    RCIR = models.TextField(_(u"Usual place of residence"), blank=True, null=True)

    # according to test.xls
    E_CODE = E_CODEField(blank=True, null=True, )

    Father_name = Char100Field(_(u"Father's Name"), blank=True, null=True)

    Mother_name = Char100Field(_(u"Mother's Name"), blank=True, null=True)

    CERT = CERTField(
        blank=True,
        null=True
    )

    Informant_name = models.TextField(
        _(u"Informant's name, address and relationship to deceased"),
        blank=True,
        null=True,
    )

    OPR = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
