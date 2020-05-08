from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resident_number = models.IntegerField(max_length=10)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)