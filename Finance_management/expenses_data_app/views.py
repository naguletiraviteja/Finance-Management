from requests import Response
from rest_framework import generics
from .models import CreateExpense,Category
from .forms import CreateExpenseForm
from django.shortcuts import render, redirect




def home(request):
    current_user = request.user
    data = CreateExpense.objects.filter(expense_user__email=current_user)
    context = {"data":data}
    return render(request,"login_app/home_page.html",context)

def create_expense(request):
        form = CreateExpenseForm()
        category = Category.objects.all()
        if request.method == "POST":
            form = CreateExpenseForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.name = form.cleaned_data['name']
                user.category = form.cleaned_data['category']
                user.description=form.cleaned_data['description']
                user.amount = form.cleaned_data['amount']
                user.expense_user = request.user
                user.save()
                return redirect("home")
        context = {"UserForm": form,"category":category}
        return render(request,'expenses_data_app/create_expense.html',context)


def edit(request,pk):
    data = CreateExpense.objects.get(id=pk)
    category = Category.objects.all()
    context = {"retrived_data":data,"category":category}
    return render(request,"expenses_data_app/edit.html",context)
