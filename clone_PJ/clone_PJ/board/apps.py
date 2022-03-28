#앱에 대한 기본 설정 정보를 담고 있는 파일
from django.apps import AppConfig


class BoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'
