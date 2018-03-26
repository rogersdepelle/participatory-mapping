import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


try:
    with open(os.path.join(BASE_DIR, 'secret_key.txt'), 'r') as f:
        SECRET_KEY = f.read().strip()
except IOError:
    try:
        import random
        SECRET_KEY = ''.join(
            [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)]
        )
        SECRECT_FILE = open(os.path.join(BASE_DIR, 'secret_key.txt'), 'w')
        SECRECT_FILE.write(SECRET_KEY)
        SECRECT_FILE.close()
    except IOError:
        Exception(
            'Please create a %s file with random characters '
            'to generate your secret key!' % 'secret_key.txt'
        )

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'mapwidgets',
    'maps',
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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'pmapping',
        'USER': 'pmapping',
        'PASSWORD': '@pmapping#',
        'CONN_MAX_AGE': 60,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

WSGI_APPLICATION = 'project.wsgi.application'

TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # NOQA
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # NOQA

APPEND_SLASH = True

MAP_WIDGETS = {
    "GooglePointFieldWidget": (
        ("zoom", 15),
        ("mapCenterLocationName", 'Campinas'),
    ),
    "GOOGLE_MAP_API_KEY": "AIzaSyDJD1wjnXh94Zcyl9Rz9Vlu50zuSTUSbw0"
}
