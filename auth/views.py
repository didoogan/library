from django.shortcuts import render
from django.http import  JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def signin(request):
    if request.method == 'POST':
        json = {}
        login = request.POST.get('login')
        password = request.POST.get('password')
        json['login'] = login
        json['password'] = password
        return JsonResponse(json)
    else:
        return render(request, 'auth/signup.html', {})


def signup(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(username=login, password=password)
        if user is not None:
            if user.is_active:
                print('User is valid, active and authenticated')
            else:
                print('The password is valid, but the account has been disabled')
        else:
            print('user and pwd are incorrct')
        print request.POST
        return render(request, 'auth/signup.html', {})
    else:
        print 'method get'
        return render(request, 'auth/signup.html', {})

