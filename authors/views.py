from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from books.models import Author
from .forms import AuthorForm


class AuthorListView(ListView):
    model = Author
    template_name = 'authors/list_author.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/detail_author.html'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('authors:list_view')
    # fields = ['first_name', 'last_name']
    template_name = 'authors/create_author.html'


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('authors:list_view')
    template_name = 'authors/delete_view.html'


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('authors:list_view')
    template_name = 'authors/update_view.html'