from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import MyUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .forms import ProfileForm

def signin(request):
    if request.method == 'POST':
        resp = {}
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                resp['success'] = True
                login(request, user)
            else:
                resp['message'] = 'The password is valid, but the account has been disabled'
        else:
            resp['message'] = 'user and password are incorrect'
        return JsonResponse(resp)
    else:
        return render(request, 'users/signup.html')


def signup(request):
    if request.user.is_authenticated():
        return redirect('card:list_view')

    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = User.objects.create_user(username, password=password)
        MyUser.objects.create(user=user)
        login(request, user)
        return redirect('card:list_view')
    else:
        return render(request, 'users/signup.html')


def logout_user(request):
    logout(request)
    return redirect('users:signup')


class UserProfile(FormView):
    form_class = ProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('card:list_view')

    def form_valid(self, form):
        user = self.request.user
        myuser = user.myuser
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['second_name']
        user.email = form.cleaned_data['email']
        user.save()
        myuser.image = form.cleaned_data['image']
        myuser.save()
        return super(UserProfile, self).form_valid(form)

    def form_invalid(self, form):
        print 'failure'






