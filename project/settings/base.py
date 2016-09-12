import djcelery
djcelery.setup_loader()

from project.settings._settings import *


CRISPY_TEMPLATE_PACK = 'bootstrap3'
ALLOWED_HOSTS = ['*']


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party apps
    'djcelery',
    'multiselectfield',
    'solo',
    'crispy_forms',
    'django_extensions',

    # Project apps
    'project.apps.dfblog',
    'project.apps.users',
)

try:
    from project.local_settings import *
except ImportError:
    pass
