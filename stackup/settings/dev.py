from common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, '/static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware','django_pdb.middleware.PdbMiddleware',)

INSTALLED_APPS += ('debug_toolbar','django_pdb')

TEMPLATE_CONTEXT_PROCESSORS += ( 'django.core.context_processors.debug',)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
