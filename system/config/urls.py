from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion API Blog",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.posts.api.routers')),
    path('api/', include('apps.users.api.routers')),
    #
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

# Debug Toolbar
if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    urlpatterns += path('__debug__/', include('debug_toolbar.urls')),
