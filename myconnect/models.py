from django.db import models

# Create your models here.
class myconnect(models.Model):
    name = models.CharField(max_length=50)
    levels = models.IntegerField(default=0)
    experience = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    domain = models.CharField(max_length=50)
    interest = models.CharField(max_length=50)
    