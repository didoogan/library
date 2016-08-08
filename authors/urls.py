from django.conf.urls import url
from views import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorDeleteView, AuthorUpdateView

urlpatterns = [
    url(r'^create_author/$', AuthorCreateView.as_view(), name='create_view'),
    url(r'^$', AuthorListView.as_view(), name='list_view'),
    url(r'^(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='detail_view'),
    url(r'^update/(?P<pk>\d+)/$', AuthorUpdateView.as_view(), name='update_view'),
    url(r'^delete/(?P<pk>\d+)/$', AuthorDeleteView.as_view(), name='delete_view'),
]

