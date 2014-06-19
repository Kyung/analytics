"""
Django settings for FittleAnalytics project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import gdata
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!e%picg=h#sew$017!-y)6xzgsrqky!c&83rat-n6l66f+@w@('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'Analytics',
    'south',
    'gdata',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'FittleAnalytics.urls'

WSGI_APPLICATION = 'FittleAnalytics.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd96o1k95jki19a',
        'HOST': 'ec2-54-204-31-13.compute-1.amazonaws.com',
        'PORT': 5432,
        'USER': 'rwfvsuilveyjkl',
        'PASSWORD': 'cAW5TJmD5GEyoichCnBpKKECZB'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_URL = '/Analytics/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "/Analytics/static"),
)

# templates
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'Analytics/templates')]

# google analytics
GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-45450760-1'

