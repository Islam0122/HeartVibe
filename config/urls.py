from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .drf_yasg import urlpatterns as swagger_urls

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/', include('apps.OTP.urls')),
                  path('api/v1/', include('apps.contactrequest.urls')),
                  path('api/v1/', include('apps.news.urls')),
                  path('api/v1/', include('apps.event.urls')),
                  path('api/v1/', include('apps.ourcommand.urls')),

              ] + swagger_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
