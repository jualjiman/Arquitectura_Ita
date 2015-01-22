"""
Django settings for arquiproject project.

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
SECRET_KEY = 'xha+p33!o#fw=ih#^=$osasl+k^7hx+zy4g0n+%i7rqaykt$_t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
     'bootstrap_admin', # always before django.contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'easy_thumbnails',
    'django.contrib.staticfiles',
    'blog',
    'ckeditor',
    

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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = '/var/www/virtual1/arquiproject/blog/static/imagenes'
MEDIA_URL = 'http://127.0.0.1:8000/static/imagenes/'

CKEDITOR_MEDIA_PREFIX = "/var/www/virtual1/arquiproject/blog/static/imagenes" #copiar ``media/ckeditor``
CKEDITOR_UPLOAD_PATH = "/media/"# Subir archivos

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'width': 'auto',

        
       
        
    },
}


THUMBNAIL_ALIASES = {
    '': {
        'noticia': {'size': (750, 400), 'crop': True},
        'noticiaG': {'size': (730, 380), 'crop': True},
        'noticiaT': {'size': (600, 250), 'crop': True},
        'slider': {'size': (1600, 500), 'crop': True},
    },
}

