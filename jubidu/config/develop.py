from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jubidu',
        'USER': 'postgres',
        'PASSWORD': 'local',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

INTERNAL_IPS = [
    '127.0.0.1',
]

SECRET_KEY = 'django-insecure-p&un2ryeeiwjo4x=g1otfyvs+0-5l^)egm89aa67-0+nf#y%=@'
