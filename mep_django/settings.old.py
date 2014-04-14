"""
Django settings for mep_django_new project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8!flv-=lu1s)k*a+6upg1q3ep91z0))-+ho3nih#nme6wqg93b'

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
    'social.apps.django_app.default', # added by chad
    #'social.apps.django_app.me', # added by chad
    #'mongoengine.django.mongo_auth', # added by chad - part of mongodoc http://mongoengine-odm.readthedocs.org/en/latest/django.html
)

#AUTH_USER_MODEL = 'mongo_auth.MongoUser' # added by chad - part of mongodoc http://mongoengine-odm.readthedocs.org/en/latest/django.html
#MONGOENGINE_USER_DOCUMENT = 'mongoengine.django.auth.User' # added by chad - part of mongodoc http://mongoengine-odm.readthedocs.org/en/latest/django.html

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mep_django_new.urls'

WSGI_APPLICATION = 'mep_django_new.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    #'default': {
    #    'ENGINE': 'django.db.backends.mongoengine',
    #    'NAME': os.path.join(BASE_DIR, 'db.mongoengine'),
    #}
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

'''
This is all added by Chad
'''

SOCIAL_AUTH_LINKEDIN_KEY = '75l485e9k29snc'
SOCIAL_AUTH_LINKEDIN_SECRET = 'iw7fONMpJZcY5HOb'

AUTHENTICATION_BACKENDS = (
    'social.backends.linkedin.LinkedinOauth',
    #'mongoengine.django.auth.MongoEngineBackend',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/logged-in/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'
SOCIAL_AUTH_LOGIN_URL = '/login-url/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/new-association-redirect-url/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account-disconnected-redirect-url/'
SOCIAL_AUTH_INACTIVE_USER_URL = '/inactive-user/'

#SOCIAL_AUTH_STORAGE = 'social.apps.django_app.me.models.DjangoStorage'

TEMPLATE_CONTEXT_PROCESSORS = (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

#SESSION_ENGINE = 'mongoengine.django.sessions'
#SESSION_SERIALIZER = 'mongoengine.django.sessions.BSONSerializer'

#SOCIAL_AUTH_USER_MODEL = 'mongoengine.django.auth.User'