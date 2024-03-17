from django.contrib import admin
from . models import Account, Transaction, Transfer
# Register your models here.

class AdminAccount(admin.ModelAdmin):
    list_display=[
        'name', 'account_type','date_created', 'balance' 
    ]
admin.site.register(Account, AdminAccount)

class AdminTransfer(admin.ModelAdmin):
    list_display=[
        'from_account', 'to_account', 'amount', 'description'
    ]
admin.site.register(Transaction)
admin.site.register(Transfer, AdminTransfer)