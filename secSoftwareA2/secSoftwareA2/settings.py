"""
Django settings for secSoftwareA2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nv)oo^@_x+3y225dw9jt89^ko2d7*=%^%!dv=*qj&=dx!&wlf4'
import django.contrib.auth


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
    'secSoftwareA2',
    'avatar',
    'axes',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.FailedLoginMiddleware',
)

ROOT_URLCONF = 'secSoftwareA2.urls'

WSGI_APPLICATION = 'secSoftwareA2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': 'root',
                'HOST': '0.0.0.0',
    }
}

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'template'),
    os.path.join(os.path.dirname(__file__), 'template/registration')
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'dhillonhoangtech@gmail.com'
EMAIL_HOST_PASSWORD = 'CoffeeCoffee1'
 
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

#axes bruteforce lockout
from datetime import timedelta
AXES_LOGIN_FAILURE_LIMIT = 5
#for testing purposes cooloff time is 60 seconds
AXES_COOLOFF_TIME = timedelta( seconds = 60 )
AXES_LOCKOUT_TEMPLATE = "lockout.html"


