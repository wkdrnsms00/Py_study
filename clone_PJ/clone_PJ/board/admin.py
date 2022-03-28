#앱에 대한 관리자 사이트에 관련된 설정
from struct import Struct
from django.contrib import admin

# Register your models here.
from .models import Student
admin.site.register(Student)