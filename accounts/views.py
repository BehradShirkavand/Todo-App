from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def user_register(request):
    if request.method == 'POST':
        form = forms.UserRegisterationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'], password=cd['password'], email=cd['email'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            messages.success(request, 'You successfully registered', 'success')
            return redirect('todo')
    else:
        form = forms.UserRegisterationForm()
    return render(request, 'register.html', {'form':form})


def user_login(request):
    if request.method == 'POST':
        form = forms.UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully', 'success')
                return redirect('todo')
            else:
                messages.error(request, 'Username or password is incorrect', 'danger')

    else:
        form = forms.UserLoginForm()
    return render(request, 'login.html', {'form':form})


def user_logout(request):
    logout(request)
    messages.success(request, "logged out succcessfully", 'success')
    return redirect('home')





