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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from yogaMaster.views import getYogaByLevel, getYogaImg, getUsrAvater, getUsrInfo, register, getResult, getStudyRecord, \
    getFavorites, getAllUsr, login, getAllYoga, addYoga, addFavorites, delFavorites, delAllFavorites
from . import settings


def getAllResult(args):
    pass


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="yogaManagement.html")),
    path('admin/', admin.site.urls),
    #小程序接口
    path('home/getYogaByLevel', getYogaByLevel),
    path('home/getYogaImg', getYogaImg),
    path('home/getResult', getResult),
    path('usr/getUsrInfo', getUsrInfo),
    path('usr/getStudyRecord', getStudyRecord),
    path('usr/getFavorites', getFavorites),
    path('usr/addFavorites', addFavorites),
    path('usr/delFavorites', delFavorites),
    path('usr/delAllFavorites', delAllFavorites),
    path('usr/register', register),
    path('usr/getUsrAvater', getUsrAvater),


    #后端管理新增接口
    path('home/getAllYoga', getAllYoga),
    path('home/addYoga', addYoga),
    path('usr/getAllUsr', getAllUsr),
    path('usr/login', login),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)