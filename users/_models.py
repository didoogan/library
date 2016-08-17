from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class MyUser(models.Model):
    user = models.OneToOneField(User)
    is_librarian = models.BooleanField(default=False)
    image = models.ImageField(blank=True, null=True)

    # def __unicode__(self):
    #     return self.get_username()

