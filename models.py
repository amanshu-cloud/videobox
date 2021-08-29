from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length = 200,default = '')
    description = models.CharField(max_length = 255,default = '')
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)
    date = models.CharField(max_length =10,default = "")
    #thumbnail = models.ImageField(upload_to = 'thumbnail_uploaded',default = None)
    #video = models.FileField(upload_to = 'videos_uploaded',validators = [FileExtensionVal])
