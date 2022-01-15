from django.db import models
from ..register.models import User
# Create your models here.


class Shops(models.Model):
    shops_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    stock = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shops'


class User(User):
    """"用户属性定义（模板中已有用户名和密码）"""


class ShoppingRecords(models.Model):
    shopping_id = models.AutoField(primary_key=True)
    id = models.ForeignKey('User', models.DO_NOTHING, db_column='id')
    shops_id = models.ForeignKey('Shops', models.DO_NOTHING, db_column='shops_id')
    nums = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'shopping_records'
