from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users import views
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('verify/email/', views.VerifyEmailView.as_view(), name='verify'),
    path('verify/code/', views.EmailCodeView.as_view(), name='code'),
    path('me/', views.ProfileView.as_view(), name="user_profile"),

    path('all/', views.AllUsersView.as_view(), name='all_users'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('restaurants/', views.RestaurantView.as_view(), name='restaurants'),

    path('category/', views.CategoryView.as_view(), name='restaurants'),
    path('menu/', views.MenuView.as_view(), name='menu'),


]