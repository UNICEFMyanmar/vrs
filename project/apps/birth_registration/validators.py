import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_2digits(value):
    if not isinstance(value, int) or not (0 < value < 100):
        raise ValidationError(_(u'%d should be two digits integer') % value)


def validate_E_CODE(value):
    if not re.match(r"[-V-Z]\d\d\.\d\d", value):
        raise ValidationError(_(u'Should be in A99.99 format'))

def validate_N_CODE(value):
    if not re.match(r"[A-Z]\d\d\.\d\d", value):
        raise ValidationError(_(u'Should be in V99.99 format'))