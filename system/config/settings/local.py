from .base import *
from . import db

# Configuraciones para Debugear consultas
from . import dev

dev.load_setting_devs(INSTALLED_APPS, MIDDLEWARE)
INTERNAL_IPS = dev.set_internal_ips()
# ***********************


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = db.SQLITE3


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR.child('static'),
]
STATIC_ROOT = BASE_DIR.child('staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

