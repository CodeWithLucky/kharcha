from django.db import models
from account.models import CustomUser
from budget.models import Category

# Create your models here.

class Account(models.Model):
    name=models.CharField(max_length=50)
    account_type=models.CharField(max_length=100)
    user_id=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    balance=models.DecimalField(max_digits=15, decimal_places=2)
    date_created=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name

class Transaction(models.Model):
    account_id=models.ForeignKey(Account, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    amount=models.DecimalField( max_digits=15, decimal_places=2)
    transaction_type=models.CharField( max_length=50)
    description=models.TextField()
    transaction_date=models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.description
    
class Transfer(models.Model):
    from_account_id=models.ForeignKey(Account, on_delete=models.CASCADE,related_name='transfers_sent')
    to_account_id=models.ForeignKey(Account, on_delete=models.CASCADE,related_name='transfer_received')
    amount=models.DecimalField(max_digits=15, decimal_places=2)
    description=models.TextField()
    transfer_date=models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.description