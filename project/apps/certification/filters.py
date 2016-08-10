import django_filters
from django_filters.filters import NumberFilter, ChoiceFilter
from django_select2 import Select2Widget
from birth_registration.codes import State_Division_Choices, District_Choices, Township_or_town_Choices, \
    Sub_code_No_Choices
from birth_registration.models import RHC
from .models import F103, F203
from django.utils.translation import ugettext_lazy as _

class FormFilter(django_filters.FilterSet):
    def extend_filter(self, field, choices):
        c = [('', _('Any')), ]
        c.extend(choices)
        self.filters[field].extra.update(
            {
                'choices': c
            }
        )



class F103Filter(FormFilter):
    f101 = NumberFilter()
    RHC = ChoiceFilter(widget=Select2Widget(), choices=RHC.objects.as_choices())

    class Meta:
        model = F103

        fields = [
            'id',
            'f101',
            'NR_SNO',
            'ST_DV',
            'DIS',
            'TWN',
            'RHC',
            'CIR',
        ]

    def __init__(self, *args, **kwargs):
        super(F103Filter, self).__init__(*args, **kwargs)

        self.extend_filter('ST_DV', State_Division_Choices)
        self.extend_filter('DIS', District_Choices)
        self.extend_filter('TWN', Township_or_town_Choices)
        self.extend_filter('CIR', Sub_code_No_Choices)



class F203Filter(FormFilter):
    f201 = NumberFilter()
    RHC = ChoiceFilter(widget=Select2Widget(), choices=RHC.objects.as_choices())

    class Meta:
        model = F203

        fields = [
            'id',
            'f201',
            'SNER',
            'NNRT',
            'NNRT1',
            'NNST',
            'RHC',
            'CIR',
        ]

    def __init__(self, *args, **kwargs):
        super(F203Filter, self).__init__(*args, **kwargs)

        self.extend_filter('NNRT', State_Division_Choices)
        self.extend_filter('NNRT1', District_Choices)
        self.extend_filter('NNST', Township_or_town_Choices)
        self.extend_filter('CIR', Sub_code_No_Choices)
