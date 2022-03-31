from contextlib import AbstractAsyncContextManager
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser) :
    comment = models.TextField() # 자기소개
    point = models.IntegerField(default=0)
    pic = models.ImageField(upload_to="user/%y/%m/%d")

    def getpic(self) :
        if self.pic :
            return self.pic.url
        return "/media/noimage.jpg"
