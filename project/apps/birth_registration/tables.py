# -*- coding: utf-8 -*-
from django.apps import apps
from django.template import Context
from django.template.loader import get_template
from django.utils.safestring import mark_safe
import django_tables2 as tables
from django_tables2.utils import A
from certification.models import F103, F203
from .models import F101, F201
from django.utils.translation import ugettext_lazy as _


class F101Table(tables.Table):
    class Meta:
        model = F101
        order_by = {'-id'}
        fields = (
            'id',
            'NR_SNO',
            'ST_DV',
            'DIS',
            'TWN',
            'RHC',
            'created_at'
        )

    id = tables.LinkColumn('F101Detail', args=[A('pk')])
    NR_SNO = tables.Column(verbose_name=_(u'Serial N.'))

    if apps.is_installed('certification'):
        certificate = tables.Column(verbose_name=_(u'Certificate'), empty_values=(), orderable=False)

    def render_certificate(self,record):

        if self.context.request.user.has_perm('certification.view_f103'):
            qs = F103.objects.filter(f101=record.id)
            count = qs.count()
            template = get_template('button_F101_to_F103.html')
            if count == 1:
                cert = qs.first().id
            else:
                cert = None
            html = template.render(Context({'count': count, 'id': record.id, 'cert': cert}))

            return mark_safe(html)
        else:
            return _("N/A")


class F101RestoreTable(F101Table):
    class Meta(F101Table.Meta):
        attrs = {'class': "F101RestoreTable"}

    id = tables.LinkColumn('F101Detail', args=[A('pk')])


class F201Table(tables.Table):

    class Meta:
        model = F201
        order_by = {'-id'}
        fields = (
            'id',
            'SNER',
            'NNRT',
            'NNRT1',
            'NNST',
            'created_at'
        )

    if apps.is_installed('certification'):
        certificate = tables.Column(verbose_name=_(u'Certificate'), empty_values=(), orderable=False)

    def render_certificate(self,record):

        if self.context.request.user.has_perm('certification.view_f203'):
            qs = F203.objects.filter(f201=record.id)
            count = qs.count()
            template = get_template('button_F201_to_F203.html')
            if count == 1:
                cert = qs.first().id
            else:
                cert = None

            html = template.render(Context({'count': count, 'id': record.id, 'cert':cert}))

            return mark_safe(html)
        else:
            return _("N/A")



    id = tables.LinkColumn('F201Detail', args=[A('pk')])
    SNER = tables.Column(verbose_name=_(u'Serial N.'))


class F201RestoreTable(F201Table):
    class Meta(F201Table.Meta):
        attrs = {'class': "F201RestoreTable"}

    id = tables.LinkColumn('F201Detail', args=[A('pk')])
