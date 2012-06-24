from common import *

DEBUG = False

if DEBUG == True:
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('apps.core.middleware.LoginRequiredMiddleware',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'birddog',
        'PORT': '6432', # PgBouncer port
        'HOST': 'data.apps.cironline.org',
        'USER': 'birddog',
        'PASSWORD': 'birddog'
    }
}

# Static
STATIC_URL = 'http://media.apps.cironline.org/birddog/site_media/'

ADMIN_MEDIA_PREFIX = 'http://media.apps.cironline.org/birddog/site_media/admin/'

# GEOS paths for GeoDjango and GDAL. Configured for our particular Heroku setup.
GEOS_LIBRARY_PATH = '/app/.geodjango/geos/lib/libgeos_c.so'
GDAL_LIBRARY_PATH = '/app/.geodjango/gdal/lib/libgdal.so'

# Caching
CACHE_MIDDLEWARE_SECONDS = 90 * 60 # 90 minutes

CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache'
    }
}
