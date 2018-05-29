# settings/local.py
from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': '',
        # 'USER': '',
        # 'PASSWORD': '',
        # 'HOST': 'localhost',
        # 'PORT': '3306',
    }
}

INSTALLED_APPS += ('debug_toolbar', )
ALLOWED_HOSTS += ('127.0.0.1', 'localhost', )
MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware', )
