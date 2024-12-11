from django.contrib import admin

from restaurants.models import RestaurantModel
from users.models import UserModel

@admin.register(RestaurantModel)
class Restaurant(admin.ModelAdmin):

    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    list_display_links = ('id', 'name')
