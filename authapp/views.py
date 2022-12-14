from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print('User is not active')
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    context = {
        'title': 'Ma Shop | AUT',
        'form': form
    }
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Ma Shop | REG',
        'form': form
    }
    return render(request, 'authapp/register.html', context)

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    user_select = request.user
    context = {
        'title': 'Geekshop | Профайл',
        'form': UserProfileForm(instance=user_select),
        #'baskets': Basket.objects.filter(user=user_select)

    }
    return render(request, 'authapp/profile.html', context)

def logout(request):
    auth.logout(request)
    return render(request, 'goddamit/index.html')
