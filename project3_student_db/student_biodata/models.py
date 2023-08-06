from django.db import models

# Create your models here.

class Student_info(models.Model):
    Name    = models.CharField(max_length=25,default='')
    Age     = models.IntegerField(default='')
    Gender  = models.CharField(max_length=10,default='')
    Address = models.CharField(max_length=50,default='')
    Email   = models.CharField(max_length=15,default='')