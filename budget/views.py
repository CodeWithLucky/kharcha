from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Budget
from finance.models import Transaction
from django.views.generic.edit import CreateView

class Budget_CreateView(CreateView):
    model = Budget
    fields = '__all__'
    template_name = 'budget/budget.html'
    success_url = '/budgets/'

    def form_valid(self, form):

        account_id = form.cleaned_data['account']
        amount = form.cleaned_data['amount']
        

        transaction = Transaction.objects.create(
            account_id=account_id,
            amount=amount,
            transaction_type='Budget Added',
            description=f'Rs.{amount} Budget added to {account_id}',
        )
        transaction.save()
        # Save the form instance first

        print(form.cleaned_data)

        response = super().form_valid(form)
        return response
        

        

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['data'] = Budget.objects.all()
    #     context['transaction'] = Transaction.objects.all()
    #     return context


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