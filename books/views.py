from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages

from books.models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/list_book.html'


class BookCreateView(CreateView):
    model = Book
    success_url = reverse_lazy('books:list_view')
    template_name = 'books/book_create.html'
    fields = ['author', 'title']

    def get_form(self, form_class=None):
        form = super(BookCreateView, self).get_form(form_class)
        for field in form.fields:
            form.fields[field].widget.attrs.update({'class': 'form-control'})
        return form

    def form_valid(self, form):
        application = form.save()
        message = u'\"%s\" has been successfully created' % application.title
        messages.success(self.request, message)
        return super(BookCreateView, self).form_valid(form)


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail_book.html'


class BookUpdateView(UpdateView):
    model = Book
    success_url = reverse_lazy('books:list_view')
    fields = ['author', 'title']
    template_name = 'books/update_book.html'

    def get_form(self, form_class=None):
        form = super(BookUpdateView, self).get_form(form_class)
        for field in form.fields:
            form.fields[field].widget.attrs.update({'class': 'form-control'})
        return form

    def form_valid(self, form):
        book = form.save()
        message = u'\"%s\" has been successfully changed' % book.title
        messages.success(self.request, message)
        return super(BookUpdateView, self).form_valid(form)


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('books:list_view')
    template_name = 'books/delete_book.html'

    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        message = u'\"%s\" has been successfully deleted' % book.title
        messages.success(self.request, message)
        return super(BookDeleteView, self).delete(request, *args, **kwargs)





