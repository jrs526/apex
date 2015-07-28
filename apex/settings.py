import os
import re


def env_flag_set(env_name):
    return os.environ.get(env_name) in {'True', '1'}


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Logging and Debugging
DEBUG = False
TEMPLATE_DEBUG = False
LOG_LEVEL = 'INFO'
if env_flag_set('DJANGO_DEBUG'):
    DEBUG = True
    TEMPLATE_DEBUG = True
    LOG_LEVEL = 'DEBUG'


# Security
SECRET_KEY = os.environ.get('DJANGO_SECRET')
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_HSTS_SECONDS = 120  # XXX Use 31536000 for production


# Honor the 'Host' header
ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.staticfiles',

    'celery',
    'rest_framework',

    'apex.app',
]


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
)


ROOT_URLCONF = 'apex.urls'


WSGI_APPLICATION = 'apex.wsgi.application'
APPEND_SLASH = False
USE_ETAGS = True


DATABASES = {}


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = 'static'


# REST API
REST_FRAMEWORK = {
    'PAGINATE_BY': 10,
}


BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'


IGNORABLE_404_URLS = (
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': LOG_LEVEL,
        'handlers': ['console'],
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': LOG_LEVEL,
        },
    },
}
