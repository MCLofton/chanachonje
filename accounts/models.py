# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    avatar=models.ImageField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    country=models.CharField(max_length=40)
    city=models.CharField(max_length=40)
    phone=models.CharField(max_length=15)
    sex=models.CharField(max_length=1,choices=((u"M",u"Male"),(u"F",u"Female")))
    birthdate=models.DateField()
    age=models.IntegerField()
    married=models.BooleanField()
    nchildren=models.IntegerField()
    employed=models.BooleanField()

