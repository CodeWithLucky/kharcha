from django.contrib import admin
from . models import Investment, InvestmentTransaction
# Register your models here.
admin.site.register(Investment)
admin.site.register(InvestmentTransaction)