from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # Add 'postgresql', 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'
        'NAME': 'my_roga', # Or path to database file if using sqlite3.
        'USER': 'my_roga',
        'HOST': 'localhost',
        'PASSWORD': 'root',
        'PORT': '5432' #Set to Empty String to Default
    }
}
