from django.contrib import admin

from admin_app.models import ManagerandCourierModel


@admin.register(ManagerandCourierModel)
class Restaurant(admin.ModelAdmin):

    list_display = ('id', 'username', 'email')
    search_fields = ('id', 'username', 'email')
    list_display_links = ('id', 'username', 'email')