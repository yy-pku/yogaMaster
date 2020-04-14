"""yoga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from yogaMaster.views import getUsrAvater, register, getFavorites, getStudyRecord, getUsrInfo, getResult, getYogaDetail, \
    getYogaList, getAllUsr, login, getAllYoga, addYoga
from . import settings


def getAllResult(args):
    pass


urlpatterns = [
    path('admin/', admin.site.urls),
    #小程序接口
    path('home/getYogaList', getYogaList),
    path('home/getYogaDetail', getYogaDetail),
    path('home/getResult', getResult),
    path('usr/getUsrInfo', getUsrInfo),
    path('usr/getStudyRecord', getStudyRecord),
    path('usr/getFavorites', getFavorites),
    path('usr/register', register),
    path('usr/getUsrAvater', getUsrAvater),

    #后端管理新增接口
    path('home/getAllYoga', getAllYoga),
    path('home/addYoga', addYoga),
    path('home/getAllResult', getAllResult),
    path('usr/getAllUsr', getAllUsr),
    path('usr/login', login),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)