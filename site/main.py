import logging
import os
import sys

# ----- MAKE SURE NO DJANGO IMPORTS BEFORE THIS -----

# Must set this env var before importing any part of Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# Use Django 1.2 as distributed with App Engine
from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.ext.webapp import util

import django.core.handlers.wsgi

# Place the directory containing this file on sys.path, the directory which
# contains all the code
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def main():
    logging.getLogger().setLevel(logging.WARNING)
    
    # Create a Django application for WSGI
    application = django.core.handlers.wsgi.WSGIHandler()

    # Run the WSGI CGI handler with that application
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
