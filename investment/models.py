from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Investment(models.Model):
    name=models.CharField(max_length=50)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    investment_type=models.CharField(max_length=50)
    value=models.DecimalField( max_digits=15, decimal_places=2)
    amount=models.DecimalField( max_digits=15, decimal_places=2)
    date_created=models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.name
    
class InvestmentTransaction(models.Model):
    investment_id=models.ForeignKey(Investment, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=15, decimal_places=2)
    transaction_type=models.CharField( max_length=50)
    description=models.TextField()
    transaction_date=models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.description