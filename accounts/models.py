# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    avatar=models.ImageField()
    user=models.ForeignKey(User)
    country=models.CharField(max_length=40)
    city=models.CharField(max_length=40)
    phone=models.CharField(max_length=15)
    sex=models.CharField()
    birthdate=models.DateField()
    age=models.IntegerField()
    married=models.BooleanField()
    nchildren=models.IntegerField()
    employed=models.BooleanField()

