from django.db import models

# Create your models here.
class User(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.CharField(unique=True, max_length=50)
    Mobile_Number = models.CharField(unique=True, max_length=10)
    Password = models.CharField(max_length=50)