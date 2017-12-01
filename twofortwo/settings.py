"""
Django settings for twofortwo project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

import dj_database_url

import raven

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!jf_xrx8jumel9-hu1dh&9w476xwhn)k^tuep405%k)13z)f5@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
  'localhost',
  'pepperclove.herokuapp.com',
  'pepperclove.club',
  'www.pepperclove.club',
]


# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'tradefood.apps.TradefoodConfig',
  'bootstrap3',
  'raven.contrib.django.raven_compat',
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'twofortwo.urls'

TEMPLATES = [
  {
      'BACKEND': 'django.template.backends.django.DjangoTemplates',
      'DIRS': [],
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

WSGI_APPLICATION = 'twofortwo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      # 'NAME': os.path.join(BASE_DIR, 'db.postgresql'),
  },
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# From heroku: https://devcenter.heroku.com/articles/django-app-configuration
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
  os.path.join(PROJECT_ROOT, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# AUTH_USER_MODEL = 'tradefood.User'

ADMINS = [
  ('Peter', 'lawsonpd@gmail.com'),
]

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'include_html': True,
#         }
#     }
# }

# config from https://docs.sentry.io/clients/python/integrations/django/
LOGGING = {
  'version': 1,
  'disable_existing_loggers': True,
  'root': {
      'level': 'WARNING',
      'handlers': ['sentry'],
  },
  'formatters': {
      'verbose': {
          'format': '%(levelname)s %(asctime)s %(module)s '
                    '%(process)d %(thread)d %(message)s'
      },
  },
  'handlers': {
      'sentry': {
          'level': 'ERROR', # To capture more than ERROR, change to WARNING, INFO, etc.
          'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
          'tags': {'custom-tag': 'x'},
      },
      'console': {
          'level': 'DEBUG',
          'class': 'logging.StreamHandler',
          'formatter': 'verbose'
      }
  },
  'loggers': {
      'django.db.backends': {
          'level': 'ERROR',
          'handlers': ['console'],
          'propagate': False,
      },
      'raven': {
          'level': 'DEBUG',
          'handlers': ['console'],
          'propagate': False,
      },
      'sentry.errors': {
          'level': 'DEBUG',
          'handlers': ['console'],
          'propagate': False,
      },
  },
}

BOOTSTRAP3 = {
  'jquery_url': 'https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js',
  'include_jquery': True,
  'javascript_in_head': True,
}

SERVER_EMAIL = 'errors@pepperclove.club'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # the default

RAVEN_CONFIG = {
  'dsn': 'https://a886e6dea3914bf8a003326e120f690b:11ec7b41fcc64521b01ac9c5980601ae@sentry.io/248118',
  # If you are using git, you can also automatically configure the
  # release based on the git info.
  # 'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
}
