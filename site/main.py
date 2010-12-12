import logging, os, sys

from google.appengine.ext.webapp import util

# Must set this env var before importing any part of Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# Remove the standard version of Django supplied with App Engine
for k in [k for k in sys.modules if k.startswith('django')]:
    del sys.modules[k]

# Force sys.path to have our own directory first, in case we want to import from it
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Force Django to reload its settings
from django.conf import settings
settings._target = None

import django.core.handlers.wsgi
import django.core.signals
import django.db
import django.dispatch.dispatcher

from django.core.signals import got_request_exception
from django.db import _rollback_on_exception

def log_exception(*args, **kwds):
    logging.exception('Exception in request:')

# Log errors
got_request_exception.connect(log_exception)

# Unregister the rollback event handler
django.dispatch.Signal().disconnect(django.db._rollback_on_exception, django.core.signals.got_request_exception)

def main():
    logging.getLogger().setLevel(logging.ERROR)
    
    # Create a Django application for WSGI
    application = django.core.handlers.wsgi.WSGIHandler()

    # Run the WSGI CGI handler with that application
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
