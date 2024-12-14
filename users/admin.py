from django.contrib import admin

from users.models import UserModel


@admin.register(UserModel)
class Restaurant(admin.ModelAdmin):

    list_display = ('id', 'username', 'email')
    search_fields = ('id', 'username', 'email')
    list_display_links = ('id', 'username', 'email')
