from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/', include('books.urls', namespace='books')),
    url(r'^authors/', include('authors.urls', namespace='authors')),
]

