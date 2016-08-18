from django.contrib import admin

from.models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    fields = ['user', 'image']

admin.site.register(MyUser, MyUserAdmin)
