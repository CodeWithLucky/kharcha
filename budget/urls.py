from django.urls import path
from . import views

urlpatterns = [
    path('budget/', views.budget_list, name='budget'),
]
