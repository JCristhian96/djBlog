from .base import os, BASE_DIR

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

SQLITE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child("config", os.getenv("DB_LOCAL")),
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_PROD_NAME"),        
        'USER': os.getenv("DB_PROD_USER"),
        'PASSWORD': os.getenv("DB_PROD_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
