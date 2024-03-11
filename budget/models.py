from django.db import models

class Category(models.Model):
    name=models.CharField( max_length=100)
    category_type=models.CharField(max_length=100)
    def _str_(self):
        return self.name

class Budget(models.Model):
    user_id=models.CharField( max_length=50)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=15, decimal_places=2)
    price_start=models.DateField(auto_now_add=True)
    price_end=models.DateField(auto_now_add=True)

    def _str_(self):
        return self.category.name 
    
    