from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # full_name = models.CharField(max_length=100, null=True, blank=True)
    #
    # def save(self, *args, **kwargs):
    #     self.full_name = '%s %s' % (self.first_name, self.last_name)
    #     super(Author, self).save(self, *args, **kwargs)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    full_name = property(get_full_name)
