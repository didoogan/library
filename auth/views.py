from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def signin(request):
    if request.method == 'POST':
        json = {}
        login = request.POST.get('login')
        password = request.POST.get('password')
        json['login'] = login
        json['password'] = password
        user = authenticate(username=login, password=password)
        if user is not None:
            if user.is_active:
                json['message'] = 'Username and password ok'
            else:
                json['message'] = 'The password is valid, but the account has been disabled'
        else:
            json['message'] = 'user and pwd are incorrect'
        return JsonResponse(json)
    else:
        return render(request, 'auth/signup.html', {})


def signup(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        user = User.objects.create_user(login, password=password)
        user.save()
        return render(request, 'books/list_book.html', {})
    else:
        return render(request, 'auth/signup.html', {})

