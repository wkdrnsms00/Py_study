#django-channels를 사용할 때 알아야 하는 개념
#data를 주고 받는 방식에 따라 사용개념이 다름
"""
ASGI config for clone_PJ project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clone_PJ.settings')

application = get_asgi_application()
