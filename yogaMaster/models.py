from django.db import models

# Create your models here.


class User(models.Model):
    class Meta:
        db_table='user'
    usrid = models.AutoField(primary_key='true')
    nickname = models.CharField(max_length=48, null='false')
    avatarUrl = models.CharField(max_length=255,default="http://127.0.0.1:8000/images/avater/buttocks.jpg")
    city = models.CharField(max_length=48)
    country = models.CharField(max_length=48)
    province = models.CharField(max_length=48)
    gender = models.IntegerField(default=1)
    language = models.CharField(max_length=48)
    lastLoginTime = models.DateField(auto_now='true')

    # def __repr__(self):
    #     return "".format(self.id,self.name)
    #
    # __str__=__repr__

class YogaImage(models.Model):
    class Meta:
        db_table='yogaImage'
    imgid = models.AutoField(primary_key='true')
    yogaName = models.CharField(max_length=48)
    level = models.IntegerField(default=1)
    imgDescription = models.CharField(max_length=255)
    image = models.ImageField(upload_to='yoga')

class Result(models.Model):
    class Meta:
        db_table='result'
    resultId = models.AutoField(primary_key='true')
    imgid = models.ForeignKey('yogaImage',on_delete=models.CASCADE)
    uploadImg = models.ImageField(upload_to='upload')
    compareImg = models.CharField(max_length=48)
    content = models.CharField(max_length=255)
    compareTime = models.DateField(auto_now='true')

class StudyRecord(models.Model):
    class Meta:
        db_table='studyRecord'
    studyRecordId = models.AutoField(primary_key='true')
    usrid = models.ForeignKey('user',on_delete=models.CASCADE)
    resultid = models.ForeignKey('result',on_delete=models.CASCADE)

class Favorites(models.Model):
    class Meta:
        db_table = 'favorites'
    favoritesId = models.AutoField(primary_key='true')
    usrid = models.ForeignKey('user',on_delete=models.CASCADE)
    imgid = models.ForeignKey('yogaImage',on_delete=models.CASCADE)
