from django.conf import settings

from django.contrib import admin

from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("auth/", include('apps.auth.urls')),
    path('tests/', include('apps.author.urls')),

    path("admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if (settings.DEBUG):
    urlpatterns.append(
        path("__debug__/", include("debug_toolbar.urls")),
    )
