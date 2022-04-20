from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.

def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('email')
            messages.success(request, 'Account was created Successfully for ' + user_name)
            return redirect('loginpage')
    context = {'form':form}
    return render(request, 'users/register1.html', context)


def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'email address or password is incorrect')
            

    context = {}
    return render(request, 'users/login1.html', context)


def logoutuser(request):
    logout(request)
    return redirect('loginpage')



@login_required(login_url = 'loginpage')
def homePage(request):
    context = {}
    return render(request, 'users/home.html', context)