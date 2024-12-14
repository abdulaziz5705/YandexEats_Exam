from django.urls import path


from restaurants import views

urlpatterns = [

    path('category/create', views.CategoryMenuView.as_view(), name='category-menu-list'),
    path('category/<int:pk>', views.CategoryMenuCRUDView.as_view(), name='category-menu-detail'),

    path('menu/create', views.CreateMenuView.as_view(), name='menu-list'),
    path('menu/<int:pk>', views.MenuCRUDView.as_view(), name='menu-detail'),

    path('me/', views.ManagerProfile.as_view(), name='manager-profile'),

]