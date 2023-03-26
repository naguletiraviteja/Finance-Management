from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "password"]
