from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages


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
    template_name = 'authors/create_author.html'

    def form_valid(self, form):
        message = super(AuthorCreateView, self).form_valid(form)
        messages .success(self.request, u'Author has been successfully created')
        return message


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('authors:list_view')
    template_name = 'authors/delete_view.html'

    success_message = u'Author has been successfully deleted'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AuthorDeleteView, self).delete(request, *args, **kwargs)


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('authors:list_view')
    template_name = 'authors/update_view.html'

    def form_valid(self, form):
        message = super(AuthorUpdateView, self).form_valid(form)
        messages .success(self.request, u'Author has been successfully edited')
        return message