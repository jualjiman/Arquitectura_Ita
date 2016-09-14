"""
Django settings for arquiproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.conf import global_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xha+p33!o#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'bootstrap_admin',  # always before django.contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'ckeditor',
    'sorl.thumbnail',
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

ROOT_URLCONF = 'arquiproject.urls'

WSGI_APPLICATION = 'arquiproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)
BOOTSTRAP_ADMIN_SIDEBAR_MENU = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'blog/static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.sep.join(
    os.path.abspath(__file__).split(os.sep)[:-2] + ['media']
)

# CKEditor settings
CKEDITOR_UPLOAD_PATH = '/media/'
CKEDITOR_JQUERY_URL = (
    '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
)
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            [
                'Bold', 'Italic',
                'Underline', 'Strike',
                'Subscript', 'Superscript',
                '-', 'RemoveFormat',
                '-', 'Table', 'HorizontalRule',
                'Link', 'Unlink'
            ],
            [
                'NumberedList', 'BulletedList',
                '-', 'Outdent', 'Indent',
                '-', 'Blockquote'
            ],
            [
                'Format', 'FontSize'
            ],
            [
                'Cut', 'Copy',
                'Paste', '-', 'Undo',
                'Redo', 'Preview'
            ],
            ['Source'],
        ],
        'skin': 'moono',
        'width': 'auto',
    }
}

# Local Settings import
try:
    from local_settings import *  # NOQA
except:
    pass
