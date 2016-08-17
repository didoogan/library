from django.conf.urls import url
# from views import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorDeleteView, AuthorUpdateView

from . import views
urlpatterns = [
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout_user, name='logout'),

]
