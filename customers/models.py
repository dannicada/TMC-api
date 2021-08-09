from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(blank=True, null=True, max_length=200)
    last_name = models.CharField(blank=True, max_length=100)
    email = models.EmailField(blank=False)
    address = models.CharField(blank=True, max_length=200)
    phone_number = models.CharField(blank=False, max_length=200)
    occupation = models.CharField(blank=True, max_length=100)
    sex = models.CharField(blank=True, max_length=10)
    account_number = models.IntegerField(blank=False)
    bvn = models.IntegerField(blank=False)
    guarantor_name = models.CharField(blank=False, max_length=100)
    guarantor_address = models.CharField(blank=False, max_length=200)
    guarantor_phone_number = models.CharField(blank=False, max_length=20)

    def __str__(self):
        return self.email

    class Meta:
        # Add verbose name
        verbose_name_plural = 'Customers'
        verbose_name = "Customer"


class Bussiness(models.Model):
    customer = models.OneToOneField(to=Customer, on_delete=models.CASCADE)
    bussiness_name = models.CharField(blank=True, max_length=200)
    address = models.CharField(blank=True, max_length=200)
    bussiness_type = models.CharField(blank=True, max_length=100)
    number_of_employees = models.IntegerField(blank=True)
    bussiness_account_number = models.IntegerField(blank=True)
    bvn = models.IntegerField(blank=True)

    def __str__(self):
        return str('bussiness owned by:', self.customer)
