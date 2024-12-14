from django.urls import path

from couriers import views

urlpatterns = [
    path('me/', views.ProfileView.as_view(), name='profile'),
]