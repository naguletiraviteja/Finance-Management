from django.urls import path
from . import views




urlpatterns = [
    path('home/',views.home,name='home'),
    path('create-expense/',views.create_expense,name='createexpense'),
    # path('edit/<int:pk>/',views.edit,name='edit')
]