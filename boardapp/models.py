from django.db import models

# Create your models here.


class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to='')
    #いいねボタンが押された回数
    good = models.IntegerField(null=True,blank=True,default=0)
    #既読した人数
    read = models.IntegerField(null=True,blank=True,default=0)
    #既読をした人の名前を保存するスペース
    readtext = models.CharField(max_length=100,null=True,default="")