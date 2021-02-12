from .base import *

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        # Add 'postgresql', 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'
        'NAME': '', # Or path to database file if using sqlite3.
        'USER': '',
        'HOST': '',
        'PASSWORD': '',
        'PORT': '' #Set to Empty String to Default
    }
}
