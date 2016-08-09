from django.shortcuts import render
from django.http import HttpResponse
from django.http import  JsonResponse


def signin(request):
    if request.method == 'POST':
        json = {}
        login = request.POST.get('login')
        password = request.POST.get('password')
        print password
        print login
        json['login'] = login
        json['password'] = password
        return JsonResponse(json)
    else:
        return render(request, 'auth/signup.html', {})


def signup(request):
    if request.method == 'POST':
        json = {}
        login = request.POST.get('login')
        password = request.POST.get('password')
        print password
        print login
        json['login'] = login
        json['password'] = password
        print request.POST
        return JsonResponse(json)
    else:
        return render(request, 'auth/signup.html', {})

