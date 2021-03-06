"""
Django settings for my_roga project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import datetime
import os
from os import path
from pathlib import Path
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
sys.path.insert(0, path.join(BASE_DIR, 'apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^oi36m$m!a)w+zox=vg7zu)b7g1ug%c6+1ycmk7vpk7ut-3u5h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'product.templatetags',
]


CUSTOM_APPS = [
    'authentication',
    'home',
    'model_catalog',
    'offer',
    'product',
    'quiz',
]

INSTALLED_APPS += CUSTOM_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_roga.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            path.join(BASE_DIR, 'my_roga', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_roga.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

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


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = 'authentication.Account'

LOGIN_URL = '/auth/login/'

LOGIN_REDIRECT_URL = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = path.join(BASE_DIR, 'static').replace('\\', '/')

STATICFILES_DIRS = (
    path.join(BASE_DIR, 'my_roga', 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = path.join(BASE_DIR, 'media').replace('\\', '/')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s - %(asctime)s - %(module)s - %(name)s - %(funcName)s() - line %(lineno)s - %(message)s'
        },
        'simple': {
            'format': '%(levelname)s - %(asctime)s - %(module)s - %(name)s - %(funcName)s() - line %(lineno)s  - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# Add all apps in logging config.
MY_LOGGERS = {}
MY_HANDLERS = {}
for app in CUSTOM_APPS:

    LOG_DIRECTORY = path.join(BASE_DIR, 'my_roga', 'logs', app)
    if not path.exists(LOG_DIRECTORY):
        os.makedirs(LOG_DIRECTORY)
    log_file_name = path.join(LOG_DIRECTORY, f"{str(datetime.date.today())}.log")

    MY_HANDLERS[app] = {
        'level': 'DEBUG',
        'class': 'logging.handlers.RotatingFileHandler',
        'filename': log_file_name,
        'formatter': 'verbose'
    }

    MY_LOGGERS[app] = {
        'handlers': [app],
        'level': 'DEBUG',
        'propagate': True,
    }

LOGGING['handlers'].update(MY_HANDLERS)
LOGGING['loggers'].update(MY_LOGGERS)