#현재 프로젝트를 서비스하기 위한 WSGL 호환 웹 서버의 진입점
#gateway interface 중 하나 
"""
WSGI config for clone_PJ project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clone_PJ.settings')

application = get_wsgi_application()
