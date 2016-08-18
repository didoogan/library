from django.contrib import admin

from .models import Card
from users.models import MyUser


# class CardAdmin(admin.ModelAdmin):

    # class MyUserInline(admin.StackedInline):
    #     model = MyUser

    # fieldsets = [
    #     (None, {'fields': ['users', 'books']}),
    #     ('Date info', {'fields': ['when_giving', 'when_return'], 'classes': ['collapse']}),
    # ]
    # inlines = [MyUserInline]

admin.site.register(Card)
