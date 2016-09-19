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
    'crispy_forms',
    'django_extensions',
    'sorl.thumbnail',

    # Project apps
    'project.apps.blog',
)

try:
    from project.local_settings import *
except ImportError:
    pass
