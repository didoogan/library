from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def signin(request):
    if request.method == 'POST':
        json = {}
        username = request.POST.get('login')
        password = request.POST.get('password')
        json['login'] = username
        json['password'] = password
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                json['message'] = 'true'
                login(request, user)
            else:
                json['message'] = 'The password is valid, but the account has been disabled'
        else:
            json['message'] = 'user and pwd are incorrect'
        return JsonResponse(json)
    else:
        return render(request, 'auth/signup.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = User.objects.create_user(username, password=password)
        user.save()
        return render(request, 'books/list_book.html')
    else:
        return render(request, 'auth/signup.html')


def logout_user(request):
    logout(request)
    return redirect('auth:signup')

