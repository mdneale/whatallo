import os

# ----- MAKE SURE NO DJANGO IMPORTS BEFORE THIS -----

# Must set this env var before importing any part of Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# Define our WSGI app
import django.core.handlers.wsgi
app = django.core.handlers.wsgi.WSGIHandler()
