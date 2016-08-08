from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from books.models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/list_book.html'


class BookCreateView(CreateView):
    model = Book
    success_url = reverse_lazy('books:list_view')
    template_name = 'books/book_create.html'
    fields = ['author', 'title']


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail_book.html'


class BookUpdateView(UpdateView):
    model = Book
    success_url = reverse_lazy('books:list_view')
    fields = ['author', 'title']
    template_name = 'books/update_book.html'


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('books:list_view')
    template_name = 'books/delete_book.html'


