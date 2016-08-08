from django.conf.urls import url
from views import BookCreateView, BookListView, BookDetailView, BookUpdateView,BookDeleteView


urlpatterns = [
    url(r'^create_book/$', BookCreateView.as_view(), name='create_view'),
    url(r'^$', BookListView.as_view(), name='list_view'),
    url(r'^(?P<pk>\d+)/$', BookDetailView.as_view(), name='detail_view'),
    url(r'^update/(?P<pk>\d+)/$', BookUpdateView.as_view(), name='update_view'),
    url(r'^delete/(?P<pk>\d+)/$', BookDeleteView.as_view(), name='delete_view'),
]

