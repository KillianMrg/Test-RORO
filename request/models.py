from django.db import models
from appli.models import UserProfileInfo

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=20)
    unit_qty = models.CharField()

class Command(models.Model):
    house=name = models.ForeignKey('UserProfileInfo', on_delete=models.CASCADE)
    command_date = models.DateField
    delivery_date = models.DateField

class Request(models.Model):
    command=name = models.ForeignKey('Command', on_delete=models.CASCADE)
    product=name = models.ForeignKey('Products', on_delete=models.CASCADE)
    qty= models.IntegerField()