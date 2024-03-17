from django.urls import path
from . import views

urlpatterns = [

    path('create_account/', views.CreateAccountView.as_view(), name='create_account'),
    path('send_money/', views.SendMoneyView.as_view(), name='send_money'),
    

]
