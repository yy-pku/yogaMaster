import os

from _pytest import logging

# Create your views here.
# -*- coding: utf-8 -*-
from django.core import serializers
from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse, HttpResponse
import simplejson
from django.shortcuts import render
from django.utils import timezone

from yoga import settings
from .models import User, YogaImage, Result, StudyRecord, Favorites


# Create your views here.

# Get    /home/getYogaByLevel                //根据level返回对应的瑜伽列表（初中高代号123）
def getYogaByLevel(request: HttpRequest):
    print(request.body)
    try:
        payload = simplejson.loads(request.body)
        level = payload['level']
        yogalist = YogaImage.objects.filter(level=level)
        # print(yogalist)
        return JsonResponse({
            'state': '200',
            'message': '获取瑜伽列表成功',
            'data': serializers.serialize('json', yogalist, ensure_ascii=False)
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()


# Get     /home/getYogaImg           //根据每个瑜伽动作文件名返回对应的图片
def getYogaImg(request: HttpRequest):
    print(request.body)
    try:
        payload = simplejson.loads(request.body)
        name = payload['yogaName']
        yogaImg = YogaImage.objects.get(yogaName=name)
        imagepath = os.path.join(settings.WEB_HOST_MEDIA_URL, str(yogaImg.image))
        return JsonResponse({
            'state': '200',
            'message': '获取瑜伽图片成功',
            'data': imagepath
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()


# Get    /usr/getUsrAvater                        //获取用户头像
def getUsrAvater(request: HttpRequest):
    print(request.body)
    try:
        payload = simplejson.loads(request.body)
        usrid = payload['usrid']
        user = User.objects.get(usrid=usrid)
        print(settings.BASE_DIR)
        print(user.usrProfile)
        imagepath = os.path.join(settings.WEB_HOST_MEDIA_URL, str(user.usrProfile))
        return JsonResponse({
            'state': '200',
            'message': '获取头像成功',
            'data': imagepath
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()


# Get    /usr/getUsrInfo                        //获取用户信息
def getUsrInfo(request: HttpRequest):
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


# post    /usr/register    //用户注册
def register(request: HttpRequest):
    try:
        user = User()
        user.usrname = request.POST.get('usrname')
        user.password = request.POST.get('password')
        user.usrProfile = request.FILES.get('usrProfile')
        res = User.objects.filter(usrname=user.usrname)
        if res.count()==0:
            user.save()
        res = User.objects.get(usrname=user.usrname).usrid
        return JsonResponse({
            'state': '200',
            'message': '登录成功',
            'usrid': res
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()


# Post    /home/getResult                    //用户根据选中的姿势上传图片得到比较结果
def getResult(request: HttpRequest):
    try:
        result = Result()
        imgid = request.POST.get('imgid')
        usrid = request.POST.get('usrid')
        result.imgid = YogaImage.objects.get(imgid=imgid)
        original = YogaImage.objects.get(imgid=imgid).image
        result.uploadImg = request.FILES.get('uploadimg')
        result.compareImg = compareYoga(result.uploadImg.url, original.url)
        result.content = 'some difference'
        result.compareTime = timezone.now()
        result.save()
        studyRecord=StudyRecord()
        studyRecord.resultid = result
        studyRecord.usrid = User.objects.get(usrid=usrid)
        studyRecord.save()
        imagepath = os.path.join(settings.WEB_HOST_MEDIA_URL, str(result.compareImg))
        return JsonResponse({
            'state': '200',
            'message': '获取结果图片成功',
            'data': imagepath,
            'content':result.content
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()


def compareYoga(uploadimg: str, original: str):
    print('compareYoga....')
    # 填充具体算法
    compareImg = "result/{}".format('a.jpg')
    return compareImg


# Get    /usr/getStudyRecord               //获取用户学习记录
def getStudyRecord(request: HttpRequest):
    print(request.body)
    try:
        urls = ''
        payload = simplejson.loads(request.body)
        usrid = payload['usrid']
        result = StudyRecord.objects.filter(usrid=usrid)
        for sr in result:
            res = Result.objects.get(resultId=sr.resultid.resultId)
            imagepath = os.path.join(settings.WEB_HOST_MEDIA_URL, str(res.compareImg))
            urls += imagepath + ','
        return JsonResponse({
            'state': '200',
            'message': '获取学习记录成功',
            'data': urls[:len(urls) - len(',')]
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()


# Post    /usr/addFavorites                     //添加用户收藏
def addFavorites(request: HttpRequest):
    print(request.body)
    try:
        favorites = Favorites()
        imgid = request.POST.get('imgid')
        usrid = request.POST.get('usrid')
        favorites.imgid = YogaImage.objects.get(imgid=imgid)
        favorites.usrid = User.objects.get(usrid=usrid)
        favorites.save()
        print(favorites)
        return JsonResponse({
            'state': '200',
            'message': '收藏成功',
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()


# Get    /usr/delFavorites                     //取消用户收藏
def delFavorites(request: HttpRequest):
    print(request.body)
    try:
        favorites = Favorites()
        imgid = request.POST.get('imgid')
        usrid = request.POST.get('usrid')
        favorites = Favorites.objects.filter(imgid=imgid).filter(usrid=usrid)
        print(favorites)
        favorites.delete()
        return JsonResponse({
            'state': '200',
            'message': '取消收藏成功',
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()

# Get    /usr/delAllFavorites                     //取消用户所有收藏
def delAllFavorites(request: HttpRequest):
    print(request.body)
    try:
        payload = simplejson.loads(request.body)
        usrid = payload['usrid']
        Favorites.objects.filter(usrid=usrid).delete()
        return JsonResponse({
            'state': '200',
            'message': '删除所有收藏成功',
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()


# Get    /usr/getFavorites                     //获取用户收藏
def getFavorites(request: HttpRequest):
    print(request.body)
    try:
        urls = ''
        payload = simplejson.loads(request.body)
        usrid = payload['usrid']
        result = Favorites.objects.filter(usrid=usrid)
        for fa in result:
            res = YogaImage.objects.get(imgid=fa.imgid.imgid)
            print(res)
            imagepath = os.path.join(settings.WEB_HOST_MEDIA_URL, str(res.image))
            urls += imagepath + ','
        return JsonResponse({
            'state': '200',
            'message': '获取收藏列表成功',
            'data': urls[:len(urls) - len(',')]
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()


# Get     /usr/getAllUsr                //获取全部用户信息列表
def getAllUsr(request: HttpRequest):
    print(request.body)
    try:
        user = User.objects.all()
        print(user)
        return JsonResponse({
            'state': '200',
            'message': '获取全部用户信息成功',
            'data': serializers.serialize('json', user, ensure_ascii=False)
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()


# Get     /usr/login                //后台管理员登录，可写死用户名密码admin/admin
def login(request: HttpRequest):
    print(request.body)
    try:
        payload = simplejson.loads(request.body)
        usrname = payload['usrname']
        password = payload['password']
        if usrname == 'admin' and password == 'admin':
            return JsonResponse({
                'state': '200',
                'message': '登录成功',
            })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()


# Get     /home/getAllYoga               //返回全部的瑜伽列表
def getAllYoga(request: HttpRequest):
    print(request.body)
    try:
        yoga = YogaImage.objects.all()
        print(yoga)
        return JsonResponse({
            'state': '200',
            'message': '获取瑜伽列表成功',
            'data': serializers.serialize('json', yoga, ensure_ascii=False)
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()


# Post     /home/addYoga               //在后端管理页面上传新的瑜伽信息
def addYoga(request: HttpRequest):
    print(request.body)
    try:
        yogaImg = YogaImage()
        yogaImg.level = request.POST.get('level')
        yogaImg.yogaName = request.POST.get('yogaName')
        yogaImg.imgDescription = request.POST.get('imgDescription')
        yogaImg.image = request.FILES.get('yogaImg')
        yogaImg.save()
        return JsonResponse({
            'state': '200',
            'message': '瑜伽图片上传成功',
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()
