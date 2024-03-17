from django.urls import path
from . import views

urlpatterns = [
    path('budgets/', views.Budget_CreateView.as_view(), name='budget'),
    # path('detail/<int:id>/', views.detail, name='detail_data'),
    # path('update/<int:id>/', views.update, name='update'),
    # path('delete/<int:id>/', views.delete_view, name='delete')
]
