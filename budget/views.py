from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Budget

# Create your views here.
@login_required
def budget_list(request):
    return render(request, 'budget/budget.html')


def add_budget(request):
    if request.method == 'POST':
        budget_title = request.POST['budget_title']
        amount = request.POST['amount']
        category = request.POST['source']
        description = request.POST['description']
        expenses = request.POST['expenses']

        budget_data = Budget.objects.create(budget_title=budget_title, amount = amount, category=category, description=description, expenses=expenses)
        budget_data.save()
        return redirect('dashboard')