from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """"用户属性定义（模板中已有用户名和密码）"""
    money = models.CharField(max_length=7, unique=False, default=9999999, verbose_name='money')

    class Meta:
        db_table = 'users'

