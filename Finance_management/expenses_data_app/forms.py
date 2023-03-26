from django import forms
from .models import CreateExpense,Category
from django.forms import ModelForm

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = CreateExpense
        fields = ['name','category','description','amount']