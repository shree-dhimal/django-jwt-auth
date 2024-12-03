from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
   
    class Meta:
        db_table = 'users' # define your custom name
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255,unique=True)
    is_deleted = models.BooleanField(default=False)