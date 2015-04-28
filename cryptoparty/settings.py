"""
Django settings for cryptoparty project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import environ
from django.core.urlresolvers import reverse_lazy

env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [x for x in env('ALLOWED_HOSTS').split(',') if x]

# Application definition

INSTALLED_APPS = (
    'flat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'debug_toolbar',

    'parties',
    'people',

    'sekizai',
    'allauth',
    'allauth.account',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'sekizai.context_processors.sekizai',
    "allauth.account.context_processors.account",
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cryptoparty.urls'

WSGI_APPLICATION = 'cryptoparty.wsgi.application'

SITE_ID = 1

DATABASES = {
    'default': env.db()
}

LANGUAGE_CODE = 'da-dk'
TIME_ZONE = 'Europe/Copenhagen'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'

src = lambda x: os.path.join(os.path.dirname(__file__), x)

STATIC_ROOT = src('static')
MEDIA_ROOT = src('media')

STATICFILES_DIRS = (
    src('static_src'),
)

TEMPLATE_DIRS = [
    src('templates'),
]

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
