from django.contrib import admin

from.models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    fields = ['user', 'image', 'is_librarian']

admin.site.register(MyUser, MyUserAdmin)
