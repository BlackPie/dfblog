import os


BASE = os.path.abspath(os.path.dirname(__name__))
STATICFILES_DIRS = (os.path.join(BASE, "static"),)
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATIC_URL = "/static/"

MEDIA_ROOT = (os.path.join(BASE, "media"))
MEDIA_URL = "/media/"
