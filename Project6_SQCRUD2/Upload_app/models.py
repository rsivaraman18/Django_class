from django.db import models

# Create your models here.

class Candidate_Profile(models.Model):
    Cname       = models.CharField(max_length=100)
    Cgender     = models.CharField(max_length=10)
    Cpdf_file   = models.FileField(upload_to='pdfs/')
    Cexcel_file = models.FileField(upload_to='excels/')
    Cimage      = models.ImageField(upload_to='images/')