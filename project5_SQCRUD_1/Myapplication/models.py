from django.db import models

# Create your models here.

class Our_datas(models.Model):
    Name    = models.CharField(max_length=25,default='')
    Dob     = models.CharField(max_length=12,default='')
    Age     = models.IntegerField(default='')
    Gender  = models.CharField(max_length=10,default='')
    State   = models.CharField(max_length=18,default='')
    Email   = models.CharField(max_length=12,default='')
    Contact = models.CharField(max_length=18,default='')
