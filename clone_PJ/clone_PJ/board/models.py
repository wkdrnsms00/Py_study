#모델에 대한 정보를 정의하고 저장하는 파일, 테이블 생성 및 테이블 필드가 정의된 파일
from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    des = models.TextField()
    def _str_(self):
        return self.name