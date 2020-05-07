# yogaMaster瑜伽大师（python+django+mysql）

## 前端页面static
用户信息：usrInfo.html  
学习记录：usrStudyRecord.html  
个人收藏：usrFav.html  
瑜伽管理：yogaManagement.html  
添加瑜伽姿势：addYoga.html

## 基础操作

>1. 数据库迁移  
python manage.py dbshell 进到数据库中，执行  
delete from django_migrations where app='your_appname';  
删除migrations文件  
python manage.py makemigrations  
python manage.py migrate
>2. 运行项目  
Python manage.py  runserver

## 接口设计

>传输 json 基本格式  
{   
"state": 200,   
"message": "success",   
"data": [  
]   
}

### 小程序接口设计

1. Get    http://127.0.0.1:8000/home/getYogaByLevel                
  //根据level返回对应的瑜伽列表（初中高代号123）  
  request：{"level":"1"}  
  Jsonresponse：  
{  
    "state": "200",  
    "message": "获取瑜伽列表成功",  
    "data": [  
        {  
            "imgid": 1,  
            "yogaName": "buttocks",  
            "level": 1,  
            "imgDescription": "buttocks",  
            "image": "http://127.0.0.1:8000/images/yoga/buttocks.jpg"  
        },  
        {  
            "imgid": 2,  
            "yogaName": "door",  
            "level": 1,  
            "imgDescription": "door",  
            "image": "http://127.0.0.1:8000/images/yoga/door.jpg"  
        }  
    ]  
}   
2. Get     http://127.0.0.1:8000/home/getYogaImg          
  //根据每个瑜伽动作文件名返回对应的图片  
  request: {"yogaName":"ayoga"}   
  Jsonresponse：  
  {  
    "state": "200",  
    "message": "获取瑜伽图片成功",  
    "data": "http://127.0.0.1:8000/images/yoga/1.jpg"  
   }

3. Get    http://127.0.0.1:8000/usr/getUsrInfo  
  //获取用户信息  
  request:   {"usrid":"1"}  
  Jsonresponse：  
  {  
    "state": "200",  
    "message": "获取用户信息成功",  
    "data": [  
        {  
            "usrid": 1,  
            "nickname": "yy",  
            "avatarUrl": "https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJfB1ibeMtSmJsQWOFuicG2G9gDDmH0syly1BpRqhm0mI7OSKK2aicibia5seyNsZYoURaA3RYUwUcE8fg/132",  
            "city": "",  
            "country": "China",  
            "province": "",  
            "gender": 2,  
            "language": "zh_CN",  
            "lastLoginTime": "2020-05-06"  
        }  
    ]  
}  

5. Post    http://127.0.0.1:8000/usr/register  
  //注册  
  var form = new FormData();  
  form.append("usrProfile", fileInput.files[0], "/C:/Users/yang/Desktop/2.jpg");  
  form.append("usrname", "yy");  
  Jsonresponse：  
  {
    "state": "200",
    "message": "登录成功",
    "usrid": 1
}

6. Post    http://127.0.0.1:8000/home/getResult  
  //用户根据选中的姿势上传图片得到比较结果图片  
  requset :  
  var form = new FormData();  
  form.append("imgid", "1");  
  form.append("usrid", "1");
  form.append("uploadimg", fileInput.files[0], "/C:/Users/yang/Desktop/3.png");  
  Jsonresponse：  
  {
    "state": "200",
    "message": "获取结果图片成功",
    "data": "http://127.0.0.1:8000/images/result/a.jpg",
    "content": "some difference"
  } 

7. Get    http://127.0.0.1:8000/usr/getStudyRecord  
  //获取用户学习记录  
  request:
  {"usrid":"1"}  
  Jsonresponse：  
   {  
  ​    "state": "200",  
  ​    "message": "获取学习记录成功",  
  ​    "data": "http://127.0.0.1:8000/yogaMaster/images/result/a.jpg,http://127.0.0.1:8000/yogaMaster/images/result/b.jpg"  
   }

8. Get    http://127.0.0.1:8000/usr/getFavorites  
  //获取用户收藏  
  request:   {"usrid":"1"}  
  Jsonresponse：  
  {  
  ​    "state": "200",  
  ​    "message": "获取收藏列表成功",  
  ​    "data": "http://127.0.0.1:8000/yogaMaster/images/yoga/1.jpg,http://127.0.0.1:8000/yogaMaster/images/yoga/2.jpg,http://127.0.0.1:8000/yogaMaster/images/yoga/3.jpg,http://127.0.0.1:8000/yogaMaster/images/yoga/4.jpg"  
   }

9. Post http://127.0.0.1:8000/usr/addFavorites  
  //添加收藏  
  requset :  
  var form = new FormData();    
  form.append("imgid", "1");
  form.append("usrid", "1");
  JsonResponse{
            'state': '200',
            'message': '收藏成功'
  }
  
10. Post http://127.0.0.1:8000/usr/delFavorites  
  //取消收藏  
  requset :  
  var form = new FormData();    
  form.append("imgid", "1");
  form.append("usrid", "1");
  JsonResponse{
            'state': '200',
            'message': '取消收藏成功'
  } 
11. Get http://127.0.0.1:8000/usr/delAllFavorites  
  //取消所有收藏  
  requset :  
  {"usrid":"1"} 
  JsonResponse{
            'state': '200',
            'message': '取消所有收藏成功'
  }
  
  11. Get http://127.0.0.1:8000/usr/ifFavorite  
  //判断是否收藏  
  requset :  
  var form = new FormData();    
  form.append("imgid", "1");
  form.append("usrid", "1");
  JsonResponse
  {
    "state": "200",
    "message": "查询收藏成功",
    "data": "1"
  }
        
### 后台管理网站接口设计

1. Get    http://127.0.0.1:8000/usr/getStudyRecord  
  //获取用户学习记录  
  request:
  {"usrid":"1"}  
  Jsonresponse：  
   {  
  ​    "state": "200",  
  ​    "message": "获取学习记录成功",  
  ​    "data": "http://127.0.0.1:8000/yogaMaster/images/result/a.jpg,http://127.0.0.1:8000/yogaMaster/images/yoga/2.jpg"  
  }
  

3. Get    http://127.0.0.1:8000/usr/getFavorites  
  //获取用户收藏  
  request:   {"usrid":"1"}  
  Jsonresponse：  
  {  
  ​    "state": "200",  
  ​    "message": "获取收藏列表成功",  
  ​    "data": "http://127.0.0.1:8000/yogaMaster/images/yoga/1.jpg,http://127.0.0.1:8000/yogaMaster/images/yoga/2.jpg,http://127.0.0.1:8000/yogaMaster/images/yoga/3.jpg,http://127.0.0.1:8000/yogaMaster/images/yoga/4.jpg"  
  }

4. Get    http://127.0.0.1:8000/usr/getAllUsr  
  //获取全部用户信息列表  
  Jsonresponse：  
  {  
    "state": "200",  
    "message": "获取全部用户信息成功",  
    "data": "[{\"model\": \"yogaMaster.user\", \"pk\": 1, \"fields\": {\"usrname\": \"yy\", \"password\": \"abc\", \"usrProfile\": \"avater/2.jpg\"}，{\"usrname\": \"yy1\", \"password\": \"abc\", \"usrProfile\": \"avater/1.jpg\"}}]"  
  }

5. (新增)  Get    http://127.0.0.1:8000/usr/login  
  //后台管理员登录，可写死用户名密码admin/admin  
  request:   
  {"usrname":"admin","password":"admin"}   
  Jsonresponse：  
   {  
  ​    "state": "200",  
  ​    "message": "登录成功"
   }

6. (新增) Get    http://127.0.0.1:8000/home/getAllYoga                
  //返回全部的瑜伽列表  
  Jsonresponse：  
  {  
    "state": "200",  
    "message": "获取瑜伽列表成功",  
    "data": "[{\"model\": \"yogaMaster.yoga\", \"pk\": \"ayoga\", \"fields\": {\"level\": 1, \"video\": \"avideourl\"}}, {\"model\": \"yogaMaster.yoga\", \"pk\": \"byoga\", \"fields\": {\"level\": 1, \"video\": \"bvideourl\"}}]"  
   }  

7. Get    http://127.0.0.1:8000/home/getYogaByLevel                
  //根据level返回对应的瑜伽列表（初中高代号123）  
  request：{"level":"1"}  
  Jsonresponse：  
  {  
    "state": "200",  
    "message": "获取瑜伽列表成功",  
    "data": "[{\"model\": \"yogaMaster.yogaimage\", \"pk\": 3, \"fields\": {\"yogaName\": \"半月式\", \"level\": 1, \"imgDescription\": \"nice\", \"image\": \"yoga/1.jpg\"}}, {\"model\": \"yogaMaster.yogaimage\", \"pk\": 9, \"fields\": {\"yogaName\": \"仰卧式\", \"level\": 3, \"imgDescription\": \"1ge\", \"image\": \"yoga/door.jpg\"}}]"  
   }  


8. (新增)  Post    http://127.0.0.1:8000/home/addYoga  
  //在后端管理页面上传新的瑜伽信息 
  requset :  
  var form = new FormData();  
  	formData.append("yogaName",document.getElementById("yoganame").value);  
		var options=("#level option:selected");    
    formData.append("level",options.val());  
		formData.append("imgDescription",document.getElementById("imgdescription").value);  
		formData.append("yogaImg",$('#image')[0].files[0]);  
    Jsonresponse：  
  {  
  ​    "state": "200",  
  ​    "message": "瑜伽图片上传成功" 
   }  


## 数据库设计

表名|属性
-|-
yogaimage|imgid：int，每个动作id（pk）
-|yogaName：varchar，瑜伽名
-|Level：int，瑜伽等级
-|imgDescription：varchar，每个动作描述
-|image：varchar，每个动作的图片文件路径
user|usrid：int，用户id（pk）
-|nickname：varchar，用户昵称
-|city：varchar，用户城市
-|country：varchar，用户国籍
-|province：varchar，用户省份
-|gender：int，用户性别
-|language：varchar，用户使用语言
-|lastLoginTime：Date，最近登录时间
-|avatarUrl：varchar，用户头像链接
studyrecord|studyRecordId：int，学习记录id（pk）
-|Usrid：int，用户id（fk）
-|resultId：int，比对结果id（fk）
favorites|favoritesId：int，收藏id （pk）
-|Usrid：int，用户id（fk）
-|imgid：int，每个动作id（fk）
result|resultId：int，比对结果id（pk）
-|imgid：int，每个动作id（fk）
-|uploadImg：varchar，用户上传图片文件路径
-|compareImg：varchar，二者比对结果图文件路径
-|content：varchar，二者比对结果描述
-|compareTime：Date，比对时间


## 一些问题说明

>1. 前后端通过json格式传输数据  
>2. 图片存储到文件夹下，数据库中存储图片路径,读取的时候先从数据库中读取路径，再到相应路径下读取图片返回，django生成model时imageFiled在数据库中就是imageField，读取时imageFiled.url。  
>3. 同一图片不同显示分辨率应需要多个尺寸  
