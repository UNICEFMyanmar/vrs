# Django settings for the project.
# add to PYTHONPATH
import sys
import os.path
import socket
from django.utils.translation import ugettext_lazy as _, ugettext

LOCAL_SETTINGS_FILE = 'settings.%s.py' % socket.gethostname().split('-')[0]
#:Host-specific settings file looks like "settings.HOSTNAME.py"

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, "static"),
)

paths = (
    PROJECT_ROOT,
    os.path.join(PROJECT_ROOT, "apps"),
)

for path in paths:
    if path not in sys.path:
        sys.path.append(path)

ADMINS = (
    ('kostik', 'kostik@kostik.net'),
)

MANAGERS = ADMINS

LANGUAGE_CODE = 'en-us'
ugettext = lambda s: s

LANGUAGES = (
    ('en', ugettext('English')),
    ('my', ugettext('Myanmar')),
)

USE_TZ = True
USE_I18N = True
USE_L10N = True


MEDIA_URL = '/media/'

STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    'reversion.middleware.RevisionMiddleware',

)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'birth_registration.context_processors.birth_registration_codes',
    'birth_registration.context_processors.installed_apps',
    'birth_registration.context_processors.raven_config_release'

)

INSTALLED_APPS = (

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'grappelli',
    'rosetta',

    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',

    'django.contrib.humanize',
    'django.contrib.webdesign',

    'bootstrap3',

    'reversion',

    'widget_tweaks',
    'django_tables2',
    'django_filters',
    'django_select2',

    'report_builder',

    'map',
    'birth_registration',
    'certification',
    'misc',
)

ROOT_URLCONF = 'project.urls'

DEFAULT_HOST = 'home'
#:django_host settings

REPORT_BUILDER_INCLUDE = ["f101", "f201", "f103", "f203"]

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

LOCALE_PATHS = (
    os.path.join(os.path.dirname(__file__), 'locale'),
)


BOOTSTRAP3 = {
    'include_jquery': True,
    'jquery_url': '//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js'
    }

GRAPPELLI_ADMIN_TITLE = _("Vital registration DB administration")
AUTO_RENDER_SELECT2_STATICS = False

#local settings go here
try:
    LOCAL_SETTINGS
except NameError:
    try:
        execfile(os.path.join(PROJECT_ROOT, LOCAL_SETTINGS_FILE), globals(), locals())
    except IOError:
        pass
    except ImportError:
        pass
