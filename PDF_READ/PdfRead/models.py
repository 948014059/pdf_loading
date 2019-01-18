from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=225,unique=True)
    emil=models.CharField(max_length=225,unique=True)
    password=models.CharField(max_length=225)
    role=models.CharField(max_length=50,default='user')
    time=models.DateTimeField(auto_now_add=True)
