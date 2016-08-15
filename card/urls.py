from django.conf.urls import url

from views import CardListView, CardCreateView, CardDeleteView

urlpatterns = [
    url(r'^$', CardListView.as_view(), name='list_view'),
    url(r'^create/$', CardCreateView.as_view(), name='create_view'),
    url(r'^delete/$', CardDeleteView.as_view(), name='delete_view'),
]
