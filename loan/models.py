from django.db import models
from customers.models import Customer
from users.models import User

# Create your models here.
class Loan(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(blank=True, max_digits=19, decimal_places=10)
    repayment_amount = models.DecimalField(blank=True, null=True, max_digits=19, decimal_places=10)
    interest = models.DecimalField(blank=True, max_digits=19, decimal_places=10)
    repaid = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    loan_type = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=False)
    due_date = models.CharField(max_length=30)
    staff = models.ForeignKey(to=User, blank=True, null=True, on_delete=models.SET_NULL)


    # def __str__(self):
    #     return str('loan by:',self.customer)

    class Meta:
        # Add verbose name
        verbose_name_plural = 'Loans'
        verbose_name = "Loan"



