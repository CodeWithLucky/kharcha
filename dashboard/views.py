from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from budget.models import Budget

# Create your views here.
@login_required
def index(request):

    total_amt = 0
    total_exp = 0

    # for budget in budgets:
    #     expense = budget.expenses
    #     total_amt += budget.amount
    #     total_exp += expense

    context = {
        'total_amount':total_amt,
        'total_expenses':total_exp,
        'remaining_balance':total_amt-total_exp,
        
        }

    return render(request, 'index.html', context)