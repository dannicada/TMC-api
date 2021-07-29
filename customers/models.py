from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(blank=True, null=True, max_length=200)
    laslt_name = models.CharField(blank=True, max_length=100)
    email = models.EmailField(blank=False)
    address = models.CharField(blank=True, max_length=200)
    phone_number = models.CharField(blank=False, max_length=200)


class Bussiness(models.Model):
