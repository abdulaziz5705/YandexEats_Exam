from django.urls import path
from admin_app import views

urlpatterns = [
    path('create/user/', views.UsersView.as_view(), name='restaurant_manager'), #BU urlsda admin manager va courierni yaratadi
    path('curier/all/', views.CourierView.as_view(), name='curier_profil'),
    path('restaurant/all/', views.RestaurantManagerView.as_view(), name='manager_profil'),
    path('login/', views.LoginView.as_view(), name='login'),

    path('create/', views.CreateRestaurantView.as_view(), name='restaurant_create'),
    path('crud/<int:pk>', views.CRUDRestaurantView.as_view(), name='restaurant_crud'),

]