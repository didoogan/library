from django.conf.urls import url
# from views import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorDeleteView, AuthorUpdateView

from . import views
urlpatterns = [
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signup/$', views.signup, name='signup'),
    # url(r'^$', AuthorListView.as_view(), name='list_view'),
    # url(r'^(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='detail_view'),
    # url(r'^update/(?P<pk>\d+)/$', AuthorUpdateView.as_view(), name='update_view'),
    # url(r'^delete/(?P<pk>\d+)/$', AuthorDeleteView.as_view(), name='delete_view'),
]

