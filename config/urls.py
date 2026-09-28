"""Root URL configuration for the O'dell Tech Shopping POS project."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pos.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler403 = 'pos.views.errors.permission_denied'
handler404 = 'pos.views.errors.page_not_found'
handler500 = 'pos.views.errors.server_error'
