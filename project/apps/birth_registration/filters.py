import django_filters
from .models import F101, F201
from django.utils.translation import ugettext_lazy as _
from .codes import State_Division_Choices, District_Choices, Township_or_town_Choices, \
    Sub_code_No_Choices


class F101Filter(django_filters.FilterSet):

    class Meta:
        model = F101
        fields = ['ST_DV', 'DIS', 'TWN', 'CIR',
                  'NR_SNO']

    def extend_filter(self, field, choices):
        c = [('', _('Any')), ]
        c.extend(choices)
        self.filters[field].extra.update(
            {
                'choices': c
            }
        )

    def __init__(self, *args, **kwargs):
        super(F101Filter, self).__init__(*args, **kwargs)

        self.extend_filter('ST_DV', State_Division_Choices)
        self.extend_filter('DIS', District_Choices)
        self.extend_filter('TWN', Township_or_town_Choices)
        self.extend_filter('CIR', Sub_code_No_Choices)


class F201Filter(django_filters.FilterSet):

    class Meta:
        model = F201
        fields = ['NNRT', 'NNRT1', 'NNST']

    def extend_filter(self, field, choices):
        c = [('', _('Any')), ]
        c.extend(choices)
        self.filters[field].extra.update(
            {
                'choices': c
            }
        )

    def __init__(self, *args, **kwargs):
        super(F201Filter, self).__init__(*args, **kwargs)

        self.extend_filter('NNRT', State_Division_Choices)
        self.extend_filter('NNRT1', District_Choices)
        self.extend_filter('NNST', Township_or_town_Choices)

