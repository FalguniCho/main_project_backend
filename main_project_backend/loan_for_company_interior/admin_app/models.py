from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *


GENDER_CHOICES = [ ('female','female'),('male','male')]

class User(AbstractUser):
    username = models.CharField(max_length=200, default='bhushan')
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    dob = models.DateField(default="2000-12-12", blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    email = models.EmailField(db_index=True, max_length=50, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    pin_code = models.IntegerField(default=0, blank=True)
    mobile = models.CharField(max_length=10)
    photo = models.ImageField(upload_to="customer/user/", default=0, blank=True)
    signature = models.ImageField(upload_to="customer/user/", default=0, blank=True)
    role = models.CharField(max_length=50, default='customer')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = Usermanager()

MARITAL_STATUS =[ ('unmarried','unmarried'),('married','married')]


class Family(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Familys')
    father_name = models.CharField(max_length=250, default=0, blank=True)
    father_profession = models.CharField(max_length=250, default=0, blank=True)
    mother_name = models.CharField(max_length=250, default=0, blank=True)
    mother_profession = models.CharField(max_length=250, default=0, blank=True)
    marital_status = models.CharField(max_length=250, choices=MARITAL_STATUS, default=0, blank=True)
    spouse_name = models.CharField(max_length=250, default=0, blank=True)
    spouse_profession = models.CharField(max_length=250, default=0, blank=True)
    mobile = models.CharField(max_length=10, default=0, blank=True)
    address = models.TextField(default=0, blank=True)



class Bank(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Banks')
    bank_name = models.CharField(max_length=250, default=0, blank=True)
    current_account_no = models.CharField(max_length=20, default=0, blank=True)
    ifsc_code = models.CharField(max_length=20, default=0, blank=True)
    passbook_copy = models.ImageField(upload_to='media/customer/bank/', default=0, blank=True) 