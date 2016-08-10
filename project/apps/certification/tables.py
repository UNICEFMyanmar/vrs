from django.contrib.auth.models import Permission
from django.template import Context
from django.template.loader import get_template
from django.utils.safestring import mark_safe
import django_tables2 as tables
from certification.models import F103, F203
from django.utils.translation import ugettext_lazy as _


class F103Table(tables.Table):
    id = tables.LinkColumn('F103DetailView', args=[tables.A('pk')])
    certificate = tables.Column(verbose_name=_(u'Certificate'), empty_values=(), orderable=False)
    f101 = tables.Column(verbose_name=_(u'F101'), empty_values=())
    NR_SNO = tables.Column(verbose_name=_(u'Serial N.'))

    def render_f101(self,record):
        if self.context.request.user.has_perm('birth_registration.view_f101'):
            template = get_template('certification/link_F103_to_F101.html')
            return mark_safe(template.render(Context({'record': record})))
        else:
            return record.f101

    def render_certificate(self, record):
        template = get_template('certification/button_F103_print.html')
        return mark_safe(template.render(Context({'record': record})))

    class Meta:
        model = F103
        order_by = {'-id'}
        fields = (
            'id',
            'f101',
            'NR_SNO',
            'ST_DV',
            'DIS',
            'TWN',
            'RHC',
            'created_at',
            'NOPR'
        )

        empty_text = get_template('certification/empty_text.html').render()

class F203Table(tables.Table):
    id = tables.LinkColumn('F203DetailView', args=[tables.A('pk')])
    SNER = tables.Column(verbose_name=_(u'Serial N.'))
    certificate = tables.Column(verbose_name=_(u'Certificate'), empty_values=(), orderable=False)
    f201 = tables.Column(verbose_name=_(u'F201'), empty_values=())

    def render_f201(self,record):
        if self.context.request.user.has_perm('birth_registration.view_f201'):
            template = get_template('certification/link_F203_to_F201.html')
            return mark_safe(template.render(Context({'record': record})))
        else:
            return record.f201

    def render_certificate(self, record):
        template = get_template('certification/button_F203_print.html')
        return mark_safe(template.render(Context({'record': record})))

    class Meta:
        model = F203
        order_by = {'-id'}
        fields = (
            'id',
            'f201',
            'SNER',
            'NNRT',
            'NNRT1',
            'NNST',
            'RHC',
            'created_at',
            'OPR'
        )

        empty_text = get_template('certification/empty_text.html').render()
