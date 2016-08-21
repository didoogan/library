import datetime

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q


from .forms import CardForm


from books.models import Book
from users.models import MyUser
from card.models import Card


class CardListView(LoginRequiredMixin, ListView):
    login_url = '/users/signup/'
    redirect_field_name = ''

    model = Card
    template_name = 'card/list_card.html'

    # def get_form(self, form_class=None):
    #     form = super(CardListView, self).get_form(self, form_class)
    #     form.fields['books'].choices = [(o.id, o.title) for o in Book.objects.filter(is_taken=False)]
    #     return form

    def get_queryset(self):
        user = self.request.user
        if user.myuser.is_librarian:
            qs = MyUser.objects.all()
            self.template_name = 'card/lib_list_card.html'
        else:
            qs = Card.objects.filter(myuser__user=user, books__is_taken=True, when_return__isnull=True)
        return qs


class CardCreateView(LoginRequiredMixin, FormView):
    login_url = '/users/signup/'
    redirect_field_name = ''
    form_class = CardForm
    template_name = 'card/create_card.html'
    success_url = '/card/'

    def get_form(self, form_class=CardForm):
        form = super(CardCreateView, self).get_form(self.form_class)
        if 'search_book' in self.request.GET:
            # form.fields['books'].choices = [(o.id, o.title) for o in Book.objects.filter(is_taken=False)]
            data = self.request.GET.get('search_value', None)
            form.fields['books'].choices = ((o.id, o.title) for o in Book.objects.filter(
                # Q(is_taken=False), Q(author__first_name__icontains=data) |
                # Q(is_taken=False), Q(author__last_name__icontains=data) |
                # Q(is_taken=False), Q(author__book__title__icontains=data)
                (Q(author__first_name__icontains=data) |
                 Q(author__last_name__icontains=data) |
                 # Q(author.unicode()=data) |
                 Q(title__icontains=data)) & Q(is_taken=False)
            ).distinct())
        else:
            form.fields['books'].choices = [(o.id, o.title) for o in Book.objects.filter(is_taken=False)]
        return form

    def form_valid(self, form):
        user = self.request.user
        myuser = user.myuser
        now = datetime.datetime.now()
        for item in form.cleaned_data['books']:
            book = Book.objects.get(id=item)
            book.is_taken = True
            book.save()
            card = Card(books=book, myuser=myuser, when_giving=now)
            card.save()
            message = u'You take \"%s\" from library' % book.title
            messages.success(self.request, message)
        return super(CardCreateView, self).form_valid(form)


class CardDeleteView(LoginRequiredMixin, FormView):
    login_url = '/users/signup/'
    redirect_field_name = ''
    form_class = CardForm
    template_name = 'card/delete_card.html'
    success_url = '/card/'

    def get_form(self, form_class=CardForm):
        user = self.request.user
        myuser = user.myuser
        form = super(CardDeleteView, self).get_form(self.form_class)
        form.fields['books'].choices = [(o.id, o.title) for o in Book.objects.filter(is_taken=True, card__myuser=myuser, card__when_return__isnull=True)]
        return form

    def form_valid(self, form):
        user = self.request.user
        myuser = user.myuser
        now = datetime.datetime.now()
        for item in form.cleaned_data['books']:
            book = Book.objects.get(id=item)
            book.is_taken = False
            book.save()
            card = Card.objects.get(books=book, myuser=myuser, when_return__isnull=True)
            card.when_return = now
            card.save()
            message = u'You return \"%s\" to library' % book.title
            messages.success(self.request, message)
        return super(CardDeleteView, self).form_valid(form)




