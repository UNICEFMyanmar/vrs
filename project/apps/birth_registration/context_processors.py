from raven.exceptions import InvalidGitRepository
from .codes import YANGON_STATE_DIVISION_CODE, YANGON_HOSPITAL_NOT_MENTIONED_CODE, ANY_HOSPITAL_CODE, SEX_MALE, \
    SEX_FEMALE
from django.conf import settings


def birth_registration_codes(request):
    return {
        'YANGON_HOSPITAL_NOT_MENTIONED_CODE': YANGON_HOSPITAL_NOT_MENTIONED_CODE,
        'YANGON_STATE_DIVISION_CODE': YANGON_STATE_DIVISION_CODE,
        'ANY_HOSPITAL_CODE': ANY_HOSPITAL_CODE,
        'SEX_MALE': SEX_MALE,
        'SEX_FEMALE': SEX_FEMALE,
        'PROJECT_PATH': settings.PROJECT_PATH  # todo: remove me
    }


def installed_apps(request):
    return {'INSTALLED_APPS': [app for app in settings.INSTALLED_APPS if not app.startswith('django')]}


def raven_config_release(request):
    if hasattr(settings, 'RAVEN_CONFIG'):
        if 'release' in settings.RAVEN_CONFIG:
                return {'REVISION': settings.RAVEN_CONFIG['release']}
    return {'REVISION': ""}