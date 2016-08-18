from django.conf.urls import url
# from views import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorDeleteView, AuthorUpdateView

from . import views
from .views import UserProfile
urlpatterns = [
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^profile/(?P<pk>\d+)$', UserProfile.as_view(), name='profile'),

]
