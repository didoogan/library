from django.conf.urls import url

from views import CardListView, CardCreateView

urlpatterns = [
    url(r'^$', CardListView.as_view(), name='list_view'),
    url(r'^create/$', CardCreateView.as_view(), name='create_view'),
]
