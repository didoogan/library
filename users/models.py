from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class MyUser(User):
    is_librarian = models.BooleanField(default=False)

    def __unicode__(self):
        self.get_username()

