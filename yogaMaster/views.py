import os
from .func import func
import cv2
import requests
import base64
import json

# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse, HttpResponse
import simplejson
from django.utils import timezone

from yoga import settings
from yoga.settings import WEB_HOST_MEDIA_URL, MEDIA_ROOT
from .models import User, YogaImage, Result, StudyRecord, Favorites


# Create your views here.

# Get    /home/getYogaByLevel                //根据level返回对应的瑜伽列表（初中高代号123）
def getYogaByLevel(request: HttpRequest):
    print(request.body)
    try:
        payload = simplejson.loads(request.body)
        level = payload['level']
        yogalist = list(YogaImage.objects.values().filter(level=level))
        print(yogalist)
        for yogaimg in yogalist:
            yogaimg['image'] = os.path.join(WEB_HOST_MEDIA_URL, str(yogaimg['image']))
        return JsonResponse({
            'state': '200',
            'message': '获取瑜伽列表成功',
            'data': yogalist
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
        print(name)
        yogaImg = YogaImage.objects.get(yogaName=name)
        imagepath = os.path.join(WEB_HOST_MEDIA_URL, str(yogaImg.image))
        print(imagepath)
        return JsonResponse({
            'state': '200',
            'message': '获取瑜伽图片成功',
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
        user = list(User.objects.values().filter(usrid=usrid))
        print(user)
        return JsonResponse({
            'state': '200',
            'message': '获取用户信息成功',
            'data': user
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()


# post    /usr/register    //用户注册
def register(request: HttpRequest):
    try:
        print(request.body)
        payload = simplejson.loads(request.body)
        nickname = payload['nickName']
        print(nickname)
        res = User.objects.filter(nickname=nickname)
        if res.count() == 0:
            user = User()
            user.nickname = nickname
            user.avatarUrl = payload['avatarUrl']
            user.city = payload['city']
            user.country = payload['country']
            user.gender = payload['gender']
            user.language = payload['language']
            user.province = payload['province']
            user.lastLoginTime = timezone.now()
            user.save()
        res = User.objects.get(nickname=nickname)
        return JsonResponse({
            'state': '200',
            'message': '登录成功',
            'usrid': res.usrid
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()



class Joint(object):
    __circle_list = []

    def __init__(self, dic):
        self.dic = dic

    def draw_line(self, img):
        # nose ---> neck
        cv2.line(img, (int(self.dic['nose']['x']), int(self.dic['nose']['y'])),
                 (int(self.dic['neck']['x']), int(self.dic['neck']['y'])), (0, 255, 0), 2)
        # nose ---> top_head
        cv2.line(img, (int(self.dic['nose']['x']), int(self.dic['nose']['y'])),
                 (int(self.dic['top_head']['x']), int(self.dic['top_head']['y'])), (0, 255, 0), 2)
        # left_eye ---> left_ear
        cv2.line(img, (int(self.dic['left_eye']['x']), int(self.dic['left_eye']['y'])),
                 (int(self.dic['left_ear']['x']), int(self.dic['left_ear']['y'])), (0, 255, 0), 2)
        # right_eye ---> right_ear
        cv2.line(img, (int(self.dic['right_eye']['x']), int(self.dic['right_eye']['y'])),
                 (int(self.dic['right_ear']['x']), int(self.dic['right_ear']['y'])), (0, 255, 0), 2)
        # right_mouth_corner ---> nose
        cv2.line(img, (int(self.dic['right_mouth_corner']['x']), int(self.dic['right_mouth_corner']['y'])),
                 (int(self.dic['nose']['x']), int(self.dic['nose']['y'])), (0, 255, 0), 2)
        # left_mouth_corner ---> nose
        cv2.line(img, (int(self.dic['left_mouth_corner']['x']), int(self.dic['left_mouth_corner']['y'])),
                 (int(self.dic['nose']['x']), int(self.dic['nose']['y'])), (0, 255, 0), 2)
        # neck --> left_shoulder
        cv2.line(img, (int(self.dic['neck']['x']), int(self.dic['neck']['y'])),
                 (int(self.dic['left_shoulder']['x']), int(self.dic['left_shoulder']['y'])), (0, 255, 0), 2)
        # neck --> right_shoulder
        cv2.line(img, (int(self.dic['neck']['x']), int(self.dic['neck']['y'])),
                 (int(self.dic['right_shoulder']['x']), int(self.dic['right_shoulder']['y'])), (0, 255, 0), 2)
        # left_shoulder --> left_elbow
        cv2.line(img, (int(self.dic['left_shoulder']['x']), int(self.dic['left_shoulder']['y'])),
                 (int(self.dic['left_elbow']['x']), int(self.dic['left_elbow']['y'])), (0, 255, 0), 2)
        # left_elbow --> left_wrist
        cv2.line(img, (int(self.dic['left_elbow']['x']), int(self.dic['left_elbow']['y'])),
                 (int(self.dic['left_wrist']['x']), int(self.dic['left_wrist']['y'])), (0, 255, 0), 2)
        # right_shoulder --> right_elbow
        cv2.line(img, (int(self.dic['right_shoulder']['x']), int(self.dic['right_shoulder']['y'])),
                 (int(self.dic['right_elbow']['x']), int(self.dic['right_elbow']['y'])), (0, 255, 0), 2)
        # right_elbow --> right_wrist
        cv2.line(img, (int(self.dic['right_elbow']['x']), int(self.dic['right_elbow']['y'])),
                 (int(self.dic['right_wrist']['x']), int(self.dic['right_wrist']['y'])), (0, 255, 0), 2)
        # neck --> left_hip
        cv2.line(img, (int(self.dic['neck']['x']), int(self.dic['neck']['y'])),
                 (int(self.dic['left_hip']['x']), int(self.dic['left_hip']['y'])), (0, 255, 0), 2)
        # neck --> right_hip
        cv2.line(img, (int(self.dic['neck']['x']), int(self.dic['neck']['y'])),
                 (int(self.dic['right_hip']['x']), int(self.dic['right_hip']['y'])), (0, 255, 0), 2)
        # left_hip --> left_knee
        cv2.line(img, (int(self.dic['left_hip']['x']), int(self.dic['left_hip']['y'])),
                 (int(self.dic['left_knee']['x']), int(self.dic['left_knee']['y'])), (0, 255, 0), 2)
        # right_hip --> right_knee
        cv2.line(img, (int(self.dic['right_hip']['x']), int(self.dic['right_hip']['y'])),
                 (int(self.dic['right_knee']['x']), int(self.dic['right_knee']['y'])), (0, 255, 0), 2)
        # left_knee --> left_ankle
        cv2.line(img, (int(self.dic['left_knee']['x']), int(self.dic['left_knee']['y'])),
                 (int(self.dic['left_ankle']['x']), int(self.dic['left_ankle']['y'])), (0, 255, 0), 2)
        # right_knee --> right_ankle
        cv2.line(img, (int(self.dic['right_knee']['x']), int(self.dic['right_knee']['y'])),
                 (int(self.dic['right_ankle']['x']), int(self.dic['right_ankle']['y'])), (0, 255, 0), 2)

    def xunhun(self, img):
        im1 = cv2.imread(img, cv2.IMREAD_COLOR)
        # im2 = cv2.resize(im1, (500,900), interpolation=cv2.INTER_CUBIC)

        for i in self.dic:
            cv2.circle(im1, (int(self.dic[i]['x']), int(self.dic[i]['y'])), 5, (0, 255, 0), -1)

        self.draw_line(im1)
        return im1


# Post    /home/getResult                    //用户根据选中的姿势上传图片得到比较结果
def getResult(request: HttpRequest):
    try:
        result = Result()
        imgid = request.POST.get('imgid')
        usrid = request.POST.get('usrid')
        print(imgid,usrid)
        result.imgid = YogaImage.objects.get(imgid=imgid)
        print(request.FILES['file'])
        result.uploadImg = request.FILES.get('file')
        result.save()
        # 上传照片title，根据这个选择评估模式
        title = YogaImage.objects.get(imgid=imgid).yogaName
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis"
        # 上传路径
        filename = os.path.join(MEDIA_ROOT, str(result.uploadImg))
        # 二进制方式打开图片文件
        f = open(filename, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        access_token = "24.85ff7b63540069f746a3a4710c353a88.2592000.1591279549.282335-19733771"
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())
            # 在用户照片上进行描点绘图
            jo = Joint(response.json()['person_info'][0]['body_parts'])
            print("jo")
            im1 = jo.xunhun(filename)
            print("im1")
            # 保存绘制结果图片
            cv2.imwrite(os.path.join(MEDIA_ROOT,'result/{}.jpg'.format(title)), im1)
            print("cv2")
            # 将json文件写入file，用来评估with open(", "w") as fp
            with open(os.path.join(MEDIA_ROOT,"file/{}.json".format(title)), "w") as fp:
                fp.write(json.dumps(response.json(), indent=4))
            # 生成结果图片,指明路径
            result.compareImg = 'result/{}.jpg'.format(title)
            # func为评估函数，返回建议contennt
            result.content = func(title)
            result.compareTime = timezone.now()
            result.save()
            studyRecord = StudyRecord()
            studyRecord.resultid = result
            studyRecord.usrid = User.objects.get(usrid=usrid)
            studyRecord.save()
            imagepath = os.path.join(WEB_HOST_MEDIA_URL, str(result.compareImg))
        else:
            print('response does not work!')
        return JsonResponse({
            'state': '200',
            'message': '获取结果图片成功',
            'data': imagepath,
            'content': result.content
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()


# Get    /usr/getStudyRecord               //获取用户学习记录
def getStudyRecord(request: HttpRequest):
    print(request.body)
    try:
        urls = []
        payload = simplejson.loads(request.body)
        usrid = payload['usrid']
        result = StudyRecord.objects.filter(usrid=usrid)
        for sr in result:
            res = Result.objects.get(resultId=sr.resultid.resultId)
            imagepath = os.path.join(WEB_HOST_MEDIA_URL, str(res.compareImg))
            urls.append(imagepath)
        return JsonResponse({
            'state': '200',
            'message': '获取学习记录成功',
            'data': urls
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
        payload = simplejson.loads(request.body)
        imgid = payload['imgid']
        usrid = payload['usrid']
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
        payload = simplejson.loads(request.body)
        imgid = payload['imgid']
        usrid = payload['usrid']
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
        urls = []
        payload = simplejson.loads(request.body)
        usrid = payload['usrid']
        result = Favorites.objects.filter(usrid=usrid)
        print(result)
        for fa in result:
            res = YogaImage.objects.get(imgid=fa.imgid.imgid)
            imagepath = os.path.join(WEB_HOST_MEDIA_URL, str(res.image))
            urls.append(imagepath)
        return JsonResponse({
            'state': '200',
            'message': '获取收藏列表成功',
            'data': urls
        })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()


# Post    /usr/ifFavorite                     //判断用户是否收藏
def ifFavorites(request: HttpRequest):
    print("if",request.body)
    try:
        payload = simplejson.loads(request.body)
        imgid = payload['imgid']
        usrid = payload['usrid']
        favorites = Favorites.objects.filter(imgid=imgid).filter(usrid=usrid)
        print(favorites)
        if favorites.count() == 0:
            return JsonResponse({
                'state': '200',
                'message': '查询收藏成功',
                'data': '0'
            })
        else:
            return JsonResponse({
                'state': '200',
                'message': '查询收藏成功',
                'data': '1'
            })
    except Exception as e:
        # logging.info(e)
        print(e)
        return HttpResponseBadRequest()


# Get     /usr/getAllUsr                //获取全部用户信息列表
def getAllUsr(request: HttpRequest):
    print(request.body)
    try:
        user = list(User.objects.values().all())
        print(user)
        return JsonResponse({
            'state': '200',
            'message': '获取全部用户信息成功',
            'data': user
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
        yogalist = list(YogaImage.objects.values().all())
        print(yogalist)
        for yogaimg in yogalist:
            yogaimg['image'] = os.path.join(WEB_HOST_MEDIA_URL, str(yogaimg['image']))
        return JsonResponse({
            'state': '200',
            'message': '获取瑜伽列表成功',
            'data': yogalist
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
