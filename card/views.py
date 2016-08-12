from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy


from card.models import Card


class CardListView(LoginRequiredMixin, ListView):
    login_url = '/auth/signup/'
    redirect_field_name = ''

    model = Card
    template_name = 'card/list_card.html'

    def get_queryset(self):
        user = self.request.user
        card = Card.objects.filter(users=user)
        return card


class CardCreateView(LoginRequiredMixin, CreateView):
    login_url = '/auth/signup/'
    redirect_field_name = ''
    model = Card
    fields = ['books']
    template_name = 'card/create_card.html'
    success_url = '/card/'

    def form_valid(self, form):
        card = form.save(commit=False)
        card.users = self.request.user
        card.books.is_taken = True
        card.save()
        return super(CardCreateView, self).form_valid(form)



