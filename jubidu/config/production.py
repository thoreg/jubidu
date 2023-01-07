import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('JUBIDU_PSQL_DB'),
        'USER': os.getenv('JUBIDU_PSQL_USER'),
        'PASSWORD': os.getenv('JUBIDU_PSQL_PASSWORD'),
        'HOST': os.getenv('JUBIDU_PSQL_HOST'),
        'PORT': os.getenv('JUBIDU_PSQL_PORT'),
    }
}

SECRET_KEY = os.getenv('JUBIDU_PRODUCTION_DJANGO_SECRET')
