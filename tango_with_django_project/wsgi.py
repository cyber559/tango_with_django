"""
WSGI config for tango_with_django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
>>>>>>> 8a1a396d807343e892f49a2fa7a604835b8f60d5
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tango_with_django_project.settings")
>>>>>>> 8a1a396d807343e892f49a2fa7a604835b8f60d5

application = get_wsgi_application()
