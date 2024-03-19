from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from finance.models import Account, Transaction

# Create your views here.
@login_required
def index(request):
    accounts = Account.objects.filter(user_id=request.user.id)


    selected_account_id = request.GET.get('account', request.session.get('selected_account_id'))

    if 'account' in request.GET:
        request.session['selected_account_id'] = selected_account_id
    if selected_account_id:
        selected_account = get_object_or_404(Account, id = selected_account_id, user_id = request.user.id)
    else:
        selected_account = accounts.first()

    transactions = Transaction.objects.all()
    

    context = {
        'accounts' : accounts,
        'selected_account' : selected_account,
        'transaction' : transactions
    }
    return render(request, 'index.html', context)