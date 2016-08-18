from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from users.models import MyUser
from django.conf import settings

from books.models import Book


class Card(models.Model):
    # users = models.ForeignKey(User)
    myuser = models.ForeignKey(MyUser, related_name='card')
    books = models.ForeignKey(Book, null=True, blank=True, related_name='card')
    when_giving = models.DateField()
    when_return = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.myuser.user.get_username()
