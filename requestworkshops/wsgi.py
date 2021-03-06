"""
WSGI config for requestworkshops project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/ubuntu/requestworkshops')
os.environ['DJANGO_SETTINGS_MODULE'] = "requestworkshops.settings"

application = get_wsgi_application()
