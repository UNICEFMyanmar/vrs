# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.utils.translation import ugettext_lazy as _
from birth_registration.apps import add_permissions_for_models


def add_view_permissions_for_f103(sender, **kwargs):
    add_permissions_for_models(app_label="certification", model__in=("f103", "f203"))


class CertificationConfig(AppConfig):
    name = 'certification'
    verbose_name = _(u'Vital registration - certification')

    def ready(self):
        post_migrate.connect(add_view_permissions_for_f103, sender=self)
