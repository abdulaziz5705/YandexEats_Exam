from django.urls import path
from admin_app import views

urlpatterns = [
    path('create/manager/', views.RestaurantManagerView.as_view(), name='restaurant_manager'),
]