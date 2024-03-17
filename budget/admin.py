from django.contrib import admin
from . models import Budget

# Register your models here.

class AdminBudget(admin.ModelAdmin):
    list_display=[
        'budget_title'
    ]
admin.site.register(Budget, AdminBudget)