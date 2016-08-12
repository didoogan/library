from __future__ import unicode_literals

from django.db import models

from authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ManyToManyField(Author)
    is_taken = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
