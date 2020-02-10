from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table='user'
    usrid = models.AutoField(primary_key='true')
    usrname = models.CharField(max_length=48, null='false')
    password = models.CharField(max_length=48, null='false')
    usrProfile = models.ImageField(upload_to='yogaMaster/images/avater')

    # def __repr__(self):
    #     return "".format(self.id,self.name)
    #
    # __str__=__repr__

class Yoga(models.Model):
    class Meta:
        db_table='yoga'
    level = models.IntegerField()
    yogaName = models.CharField(max_length=48,primary_key='true')
    video = models.URLField()

class YogaImage(models.Model):
    class Meta:
        db_table='yogaImage'
    imgid = models.AutoField(primary_key='true')
    yogaName = models.ForeignKey('yoga',on_delete=models.CASCADE)
    imgDescription = models.CharField(max_length=255)
    image = models.ImageField()

class Result(models.Model):
    class Meta:
        db_table='result'
    resultId = models.AutoField(primary_key='true')
    imgid = models.ForeignKey('yogaImage',on_delete=models.CASCADE)
    uploadImg = models.ImageField(upload_to='yogaMaster/images/upload')
    compareImg = models.ImageField(upload_to='yogaMaster/images/result')
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
