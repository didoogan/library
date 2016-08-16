from django.contrib import admin

from .models import Card


class CardAdmin(admin.ModelAdmin):
    fields = ('users', 'books', 'when_giving', 'when_return')

admin.site.register(Card, CardAdmin)
