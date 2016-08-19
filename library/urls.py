from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from books.views import BookListView


urlpatterns = [
    url(r'^$', BookListView.as_view(),  name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^books/', include('books.urls', namespace='books')),
    url(r'^authors/', include('authors.urls', namespace='authors')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^card/', include('card.urls', namespace='card')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
