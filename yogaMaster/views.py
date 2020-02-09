from _pytest import logging

# Create your views here.
# -*- coding: utf-8 -*-
from django.core import serializers
from django.http import HttpRequest,HttpResponseBadRequest,JsonResponse
import simplejson
from .models import User,Yoga,YogaImage,Result,StudyRecord,Favorites

# Create your views here.
# Get     /home/getYogaList&level                //根据level返回对应的瑜伽列表（初中高代号123）
# Get     /home/getYogaDetail&name          //根据瑜伽名返回对应的分解动作及视频详情
# Post    /home/getResult&imgid                    //用户根据选中的姿势上传图片得到比较结果
# Get    /usr/getUsrInfo&usrid                        //获取用户信息
# Get    /usr/getStudyRecord&usrid               //获取用户学习记录
# Get    /usr/getFavorites&usrid                     //获取用户收藏

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

#标记进度

def getYogaDetail(request:HttpRequest):
    print(request.body)
    try:
        payload = simplejson.loads(request.body)
        yogaName = payload['yogaName']
        yogaImage = YogaImage.Objects.filter(yogaName_id=yogaName)
        return JsonResponse({
            'state': '200',
            'message': '获取瑜伽详情成功',
            'data': serializers.serialize('json', yogaImage, ensure_ascii=False)
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()

def getResult(request:HttpRequest):
    # print(request.body)
    try:
        payload = simplejson.loads(request.body)
        imgid_id = payload['imgid']
        Result.Objects.filter(imgid_id=imgid_id)
    except Exception as e:
        logging.info(e)
        return HttpResponseBadRequest()

def getUsrInfo(request:HttpRequest):
    # print(request.body)
    try:
        payload = simplejson.loads(request.body)
        usrid = payload['usrid']
        User.Objects.filter(usrid=usrid)
    except Exception as e:
        logging.info(e)
        return HttpResponseBadRequest()

def getStudyRecord(request:HttpRequest):
    # print(request.body)
    try:
        payload = simplejson.loads(request.body)
        usrid = payload['usrid']
        StudyRecord.Objects.filter(usrid_id=usrid)
    except Exception as e:
        logging.info(e)
        return HttpResponseBadRequest()

def getFavorites(request:HttpRequest):
    # print(request.body)
    try:
        payload = simplejson.loads(request.body)
        usrid = payload['usrid']
        Favorites.Objects.filter(usrid_id=usrid)
    except Exception as e:
        logging.info(e)
        return HttpResponseBadRequest()