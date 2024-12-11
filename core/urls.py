from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Instagram JWT API",
        default_version='v1',
        description="API for Instagram JWT",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin', admin.site.urls),
    path('users/', include('users.urls')),
    path('restaurants/', include('restaurants.urls')),
    path('manager/', include('admin_app.urls')),
    re_path(r'^swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
