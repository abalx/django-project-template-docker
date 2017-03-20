# coding: utf-8

import os
import glob

ROOT_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '../..'))
SERVER_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
CLIENT_DIR = os.path.normpath(os.path.join(ROOT_DIR, 'client'))
CLIENT_APPS_DIR = os.path.normpath(os.path.join(CLIENT_DIR, 'apps'))

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'ckeditor',

    'apps.core',
    'apps.users',
)

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': os.environ.get('POSTGRES_DB'),
         'USER': os.environ.get('POSTGRES_USER'),
         'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
         'HOST': 'db',
         'PORT': os.environ.get('POSTGRES_PORT'),
     }
}

ALLOWED_HOSTS = []

SITE_ID = 1

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'apps.core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': glob.glob(CLIENT_APPS_DIR + r'/*/templates'),
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'apps.core.wsgi.application'

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(CLIENT_DIR, 'static_root')

STATICFILES_DIRS = [
    ('vendor', os.path.join(CLIENT_DIR, 'vendor')),
    ('build', os.path.join(CLIENT_DIR, 'build')),
]
STATICFILES_DIRS += glob.glob(CLIENT_APPS_DIR + r'/*/static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(CLIENT_DIR, 'media_root')

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

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
    'default': {
        'forcePasteAsPlainText': True,
        'allowedContent': True,
        'language': 'ru',
        'toolbar': [
            ['Bold', 'Italic', 'Underline'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Format'],
            [
                'NumberedList', 'BulletedList',
                'Outdent', 'Indent', 'Image', 'Table'
            ],
            ['Link', 'Unlink'],
            ['Blockquote', 'Youtube'],
            ['CodeSnippet'],
            ['Source'],
            ['Undo', 'Redo'],
        ],
        'uiColor': '#FFFFFF',
        'extraPlugins': ','.join(
            [
                'codesnippet',
            ]),
    },
}

AUTH_USER_MODEL = "users.User"