from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
"""Swagger authorization yaxshi  ishlamadi shunga hamma apilarni postmanda tekshirdim"""
schema_view = get_schema_view(
    openapi.Info(
        title="Yandex Eats",
        default_version='v1',
        description="Api for Yandex Eats",
    ),
    public=True,
    permission_classes=[AllowAny],
    authentication_classes=[SessionAuthentication, BasicAuthentication, JWTAuthentication],
)
urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),

    path('admin', admin.site.urls),
    path('users/', include('users.urls')),

    path('manager/', include('admin_app.urls')),
    path('restaurants/', include('admin_app.urls')),

    path('couriers/', include('couriers.urls')),

    path('restaurants/', include('restaurants.urls')),

    path('orders/', include('orders.urls'))
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
