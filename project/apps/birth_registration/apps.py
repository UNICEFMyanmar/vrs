# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.utils.translation import ugettext_lazy as _
from birth_registration.permissions import create_location_related_permissions


def add_permissions_for_f101_f210(**kwargs):
    add_permissions_for_models(app_label="birth_registration", model__in=("f101", "f201"))

def add_permissions_for_models(app_label, model__in):
    content_types = ContentType.objects.filter(app_label=app_label, model__in=model__in)
    if not content_types.count() == len(model__in):
        raise ContentType.DoesNotExist("Found %s, expected 4" % content_types.count())
    for content_type in content_types:
        codename = "view_%s" % content_type.model

        if not Permission.objects.filter(content_type=content_type, codename=codename):
            Permission.objects.create(content_type=content_type,
                                      codename=codename,
                                      name="Can view %s" % content_type.name)
            if settings.DEBUG:
                print "Added view permission for %s" % content_type.name
        else:
            if settings.DEBUG:
                print "Permission already exists for %s" % content_type.name

    create_location_related_permissions(ContentType.objects.get(app_label="birth_registration", model="f101"), True)
    print "Added location-related permissions  for f101"


class BirthRegistrationConfig(AppConfig):
    name = 'birth_registration'
    verbose_name = _(u'Vital registration')

    def ready(self):
        post_migrate.connect(add_permissions_for_f101_f210, sender=self)
