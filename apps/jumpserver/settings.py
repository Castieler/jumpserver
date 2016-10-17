"""
Django settings for jumpserver project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import sys

from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)

sys.path.append(PROJECT_DIR)

# Import project config setting
try:
    from config import config as env_config, env

    CONFIG = env_config.get(env, 'default')()
except ImportError:
    CONFIG = type('_', (), {'__getattr__': None})()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG.SECRET_KEY or '2vym+ky!997d5kkcc64mnz06y1mmui3lut#(^wd=%s_qj$1%x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = CONFIG.DEBUG or False


# Absolute url for some case, for example email link
SITE_URL = CONFIG.SITE_URL or 'http://localhost'


# LOG LEVEL
LOG_LEVEL = 'DEBUG' if DEBUG else CONFIG.LOG_LEVEL or 'WARNING'

ALLOWED_HOSTS = CONFIG.ALLOWED_HOSTS or []

# Application definition

INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'assets.apps.AssetsConfig',
    'perms.apps.PermsConfig',
    'ops.apps.OpsConfig',
    'audits.apps.AuditsConfig',
    'common.apps.CommonConfig',
    'terminal.apps.TerminalConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'bootstrapform',
    'captcha',
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jumpserver.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'ws4redis.context_processors.default',
            ],
        },
    },
]

# WSGI_APPLICATION = 'jumpserver.wsgi.application'

LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGIN_URL = reverse_lazy('users:login')

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

if CONFIG.DB_ENGINE == 'sqlite':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': CONFIG.DB_NAME or os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.%s' % CONFIG.DB_ENGINE,
            'NAME': CONFIG.DB_NAME,
            'HOST': CONFIG.DB_HOST,
            'PORT': CONFIG.DB_PORT,
            'USER': CONFIG.DB_USER,
            'PASSWORD': CONFIG.DB_PASSWORD,
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
#
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

# Logging setting
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'main': {
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'format': '%(asctime)s [%(module)s %(levelname)s] %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'main'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'main',
            'filename': os.path.join(PROJECT_DIR, 'logs', 'jumpserver.log')
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': False,
            'level': LOG_LEVEL,
        },
        'django.request': {
            'handlers': ['console', 'file'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
        'django.server': {
            'handlers': ['console', 'file'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
        'jumpserver': {
            'handlers': ['console', 'file'],
            'level': LOG_LEVEL,
        },
        'jumpserver.users.api': {
            'handlers': ['console', 'file'],
            'level': LOG_LEVEL,
        },
        'jumpserver.users.view': {
            'handlers': ['console', 'file'],
            'level': LOG_LEVEL,
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# I18N translation
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'), ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Media files (File, ImageField) will be save these

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/') + '/'

# Use django-bootstrap-form to format template, input max width arg
BOOTSTRAP_COLUMN_COUNT = 11

# Init data or generate fake data source for development
FIXTURE_DIRS = [os.path.join(BASE_DIR, 'fixtures'), ]

# Email config
EMAIL_HOST = CONFIG.EMAIL_HOST
EMAIL_PORT = CONFIG.EMAIL_PORT
EMAIL_HOST_USER = CONFIG.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = CONFIG.EMAIL_HOST_PASSWORD
EMAIL_USE_SSL = CONFIG.EMAIL_USE_SSL
EMAIL_USE_TLS = CONFIG.EMAIL_USE_TLS
EMAIL_SUBJECT_PREFIX = CONFIG.EMAIL_SUBJECT_PREFIX

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
        'users.backends.IsValidUser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'users.backends.TerminalAuthentication',
    ),
}
# This setting is required to override the Django's main loop, when running in
# development mode, such as ./manage runserver
# WSGI_APPLICATION = 'ws4redis.django_runserver.application'

# URL that distinguishes websocket connections from normal requests
# WEBSOCKET_URL = '/ws/'

# WebSocket Redis
# WS4REDIS_CONNECTION = {
#     'host': CONFIG.REDIS_HOST or '127.0.0.1',
#     'port': CONFIG.REDIS_PORT or 6379,
#     'db': 2,
# }

# Set the number of seconds each message shall persisted
# WS4REDIS_EXPIRE = 3600

# WS4REDIS_HEARTBEAT = 'love you'

# WS4REDIS_PREFIX = 'demo'

# SESSION_ENGINE = 'redis_sessions.session'

# SESSION_REDIS_PREFIX = 'session'

# SESSION_REDIS_HOST = CONFIG.REDIS_HOST

# SESSION_REDIS_PORT = CONFIG.REDIS_PORT

# SESSION_REDIS_PASSWORD = CONFIG.REDIS_PASSWORD

# SESSION_REDIS_DB = CONFIG.REDIS_DB


# Custom User Auth model
AUTH_USER_MODEL = 'users.User'

# Celery using redis as broker
BROKER_URL = 'redis://%(password)s%(host)s:%(port)s/3' % {
    'password': CONFIG.REDIS_PASSWORD + ':' if CONFIG.REDIS_PASSWORD else '',
    'host': CONFIG.REDIS_HOST or '127.0.0.1',
    'port': CONFIG.REDIS_PORT or 6379,
}
CELERY_RESULT_BACKEND = BROKER_URL

# Captcha settings, more see https://django-simple-captcha.readthedocs.io/en/latest/advanced.html
CAPTCHA_IMAGE_SIZE = (75, 33)
CAPTCHA_FOREGROUND_COLOR = '#001100'

#

