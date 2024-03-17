from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Budget
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView


# Create your views here

class Budget_CreateView(CreateView):
    model = Budget
    fields = '__all__'
    template_name = 'budget/budget.html'
    success_url = '/budgets/'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = Budget.objects.all()
        return context
    

# def budget_list(request):
#     if request.method == 'POST':
#         budget_title = request.POST['budget_title']
#         amount = request.POST['amount']
#         category = request.POST['category']
#         description = request.POST['description']
#         expenses = request.POST['expenses']
#         budget_data = Budget.objects.create(user_id=request.user, budget_title=budget_title, amount = amount, category=category, description=description, expenses=expenses)
#         print(budget_data)
#         budget_data.save()
#         return redirect('budget')
    
#     data = Budget.objects.all()
#     return render(request, 'budget/budget.html', {'data':data})


# def detail(request, id):
#     # Retrieve a single Budget object with the given id
#     one_data = get_object_or_404(Budget, id=id)
#     return render(request, 'budget/detail.html', {'one': one_data})
    

# def update(request, id):
#     data = Budget.objects.all()
#     budget_instance = Budget.objects.get(id=id)
#     if request.method == 'POST':
#         budget_instance.budget_title = request.POST['budget_title']
#         budget_instance.amount = request.POST['amount']
#         budget_instance.category = request.POST['category']
#         budget_instance.description = request.POST['description']
#         budget_instance.expenses = request.POST['expenses']
#         budget_instance.save()
#         return redirect('budget')
    
#     return render(request, 'budget/budget.html', {'data':data, 'update': budget_instance })

# @login_required
# def delete_view(request, id):
#     data = Budget.objects.get(id = id)
#     data.delete()
#     return redirect('budget')