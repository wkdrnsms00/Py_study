#현재 Django 프로젝트의 URL 선언을 저장
#사용자가 url로 django에 접근하면 들어온 url로 rul 규칙을 보고 내부에 일치하는 View를 찾아 연결

# """clone_PJ URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include('App1.urls'))
# ]
#-*- coding:EUC-kr-*-
from django.contrib import admin
from django.urls import include, path
from board.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index')

]
