from .base import os, BASE_DIR

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

SQLITE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child("config", os.getenv("DB_LOCAL")),
    }
}
