from django.shortcuts import render
from django.views.generic import CreateView
from .models import Transfer, Account, Transaction

class SendMoneyView(CreateView):
    template_name = 'finance/send_money.html'
    model = Transfer
    fields = '__all__'
    success_url = '/'

    def form_valid(self, form):
        amount = form.cleaned_data['amount']
        from_account = form.cleaned_data['from_account']
        to_account = form.cleaned_data['to_account']

        if from_account.balance >= amount:
            from_account.balance -= amount
            to_account.balance += amount
            from_account.save()
            to_account.save()

            # Create transaction for money transfer
            transaction = Transaction.objects.create(
                account_id=from_account,
                amount=amount,
                transaction_type='Money Transfer',
                description=f'Transferred Rs.{amount} to {to_account}',
            )
            transaction.save()
            return super().form_valid(form)
        else:
            form.add_error(None, 'Insufficient balance.')
            return self.form_invalid(form)


class CreateAccountView(CreateView):
    template_name = 'finance/create_account.html'
    model = Account
    fields = '__all__'
    success_url = '/'