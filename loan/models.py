from django.db import models

# Create your models here.
class Loan(models.Model):
    amount = models.IntegerField(blank=True)
    repayment_amount = models.IntegerField(blank=True)
    interest = models.FloatField(blank=True)
    repaid = models.BooleanField(default=False)

