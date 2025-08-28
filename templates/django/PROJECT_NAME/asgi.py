"""
ASGI config for PROJECT_NAME project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROJECT_NAME.settings')

application = get_asgi_application()
