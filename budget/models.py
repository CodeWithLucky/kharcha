from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField( max_length=100)
    category_type=models.CharField(max_length=100)
    def _str_(self):
        return self.name

class Budget(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    budget_title = models.CharField(max_length=100,null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=15, decimal_places=2,null=True)
    description = models.TextField(null=True)
    expenses = models.CharField(max_length=50,null=True)


    def _str_(self):
        return self.category.name 
    
    