# from django.db import models

# # Create your models here.


# class User(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     username = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     staff_status = models.BooleanField()

#     def __str__(self):
#         return self.username


# class IpoInfo(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     company_logo_path = models.TextField()
#     company_name = models.CharField(max_length=255)
#     price_band = models.CharField(max_length=255)
#     open = models.CharField(max_length=255)
#     close = models.CharField(max_length=255)
#     issue_size = models.CharField(max_length=255)
#     issue_type = models.CharField(max_length=255)
#     listing_date = models.CharField(max_length=255)
#     status = models.CharField(max_length=255)
#     ipo_price = models.CharField(max_length=255)
#     listing_price = models.CharField(max_length=255)
#     listing_gain = models.CharField(max_length=255)
#     cmp = models.CharField(max_length=255)
#     current_return = models.CharField(max_length=255)
#     rhp = models.CharField(max_length=255)
#     drhp = models.CharField(max_length=255)

#     def __str__(self):
#         return self.company_name

from django.contrib.auth.models import User

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

class IpoInfo(models.Model):
    company_name = models.CharField(max_length=255)
    listing_date = models.DateField()