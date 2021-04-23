from django.db import models

# Create your models here.
class Matche(models.Model):
    mdate=models.DateField()
    mmatch=models.CharField(max_length=64)
    mtime=models.TimeField()
    mvenue=models.CharField(max_length=64)
    mmypred=models.CharField(max_length=64)
