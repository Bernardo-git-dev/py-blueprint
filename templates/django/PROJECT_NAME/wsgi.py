"""
WSGI config for PROJECT_NAME project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROJECT_NAME.settings')

application = get_wsgi_application()
