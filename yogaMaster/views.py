import os

from _pytest import logging

# Create your views here.
# -*- coding: utf-8 -*-
from django.core import serializers
from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse, HttpResponse
import simplejson

from yoga import settings
from .models import User,Yoga,YogaImage,Result,StudyRecord,Favorites

# Create your views here.

# Get     /home/getYogaList                //根据level返回对应的瑜伽列表（初中高代号123）
def getYogaList(request:HttpRequest):
    print(request.body)
    try:
        payload = simplejson.loads(request.body)
        level = payload['level']
        yogalist = Yoga.objects.filter(level=level)
        print(yogalist)
        return JsonResponse({
            'state': '200',
            'message': '获取瑜伽列表成功',
            'data': serializers.serialize('json', yogalist, ensure_ascii=False)
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()

# Get     /home/getYogaDetail           //根据每个瑜伽动作文件名返回对应的图片
def getYogaDetail(request:HttpRequest):
    print(request.body)
    try:
        payload = simplejson.loads(request.body)
        filename = payload['filename']
        imagepath = os.path.join(settings.BASE_DIR, "yogaMaster\images\yoga\{}".format(filename))
        print(imagepath)
        with open(imagepath, 'rb') as f:
            image_data = f.read()
        return HttpResponse(image_data, content_type="image/png")
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()

# Get    /usr/getUsrAvater                        //获取用户头像
def getUsrAvater(request:HttpRequest):
    print(request.body)
    try:
        payload = simplejson.loads(request.body)
        usrid = payload['usrid']
        user = User.objects.get(usrid=usrid)
        imagepath = os.path.join(settings.BASE_DIR, user.usrProfile.url)
        print(imagepath)
        with open(imagepath, 'rb') as f:
            image_data = f.read()
        return HttpResponse(image_data, content_type="image/png")
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()

# Get    /usr/getUsrInfo                        //获取用户信息
def  getUsrInfo(request:HttpRequest):
    print(request.body)
    try:
        payload = simplejson.loads(request.body)
        usrid = payload['usrid']
        user = User.objects.filter(usrid=usrid)
        print(user)
        return JsonResponse({
        'state': '200',
        'message': '获取用户信息成功',
        'data': serializers.serialize('json', user, ensure_ascii=False)
    })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()

#post    /usr/register    //注册
def register(request:HttpRequest):
    try:
        user = User()
        user.usrid = request.POST.get('usrid')
        user.usrname = request.POST.get('usrname')
        user.password = request.POST.get('password')
        user.usrProfile = request.FILES.get('usrProfile')
        user.save()

        return JsonResponse({
            'state': '200',
            'message': '注册成功',
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()

# 标记进度
# Post    /home/getResult                    //用户根据选中的姿势上传图片得到比较结果
def getResult(request:HttpRequest):
    print(request.body)
    try:
        payload = simplejson.loads(request.body)
        imgid_id = payload['image']
        Result.objects.filter(imgid_id=imgid_id)
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()


# Get    /usr/getStudyRecord               //获取用户学习记录
def getStudyRecord(request:HttpRequest):
    print(request.body)
    try:
        payload = simplejson.loads(request.body)
        usrid = payload['usrid']
        StudyRecord.objects.filter(usrid_id=usrid)
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()

# Get    /usr/getFavorites                     //获取用户收藏
def getFavorites(request:HttpRequest):
    print(request.body)
    try:
        payload = simplejson.loads(request.body)
        usrid = payload['usrid']
        Favorites.objects.filter(usrid_id=usrid)
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()