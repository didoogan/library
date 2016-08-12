from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from books.models import Book


class Card(models.Model):
    users = models.ForeignKey(to=settings.AUTH_USER_MODEL)
    books = models.ForeignKey(Book, null=True, blank=True)
    when_giving = models.DateField(auto_now_add=True)
    when_return = models.DateField(null=True, blank=True)
