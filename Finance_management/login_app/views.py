from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect("home")
    context = {"UserForm": form}
    return render(request, "login_app/register.html", context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect("/home")
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(username=email,email=email, password=password)
        except:
            # messages.error(request, "username doesnot exists")
            pass

        user = authenticate(request, username=email,email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            # messages.error(request, "username  or password is incorrect")
            pass

    return render(request, "login_app/login_page.html")


def logoutuser(request):
    logout(request)
    return redirect('login')



