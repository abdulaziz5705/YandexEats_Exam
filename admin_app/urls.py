from django.urls import path
from admin_app import views

urlpatterns = [
    path('create/manager/curiers/', views.UsersView.as_view(), name='restaurant_manager'),
    path('curier/profil/', views.CourierView.as_view(), name='curier_profil'),
    path('manager/profil/', views.RestaurantManagerView.as_view(), name='manager_profil'),
    path('login/', views.LoginView.as_view(), name='login'),
]