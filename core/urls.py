from django.conf import settings

from django.contrib import admin

from django.conf.urls.static import static
from django.urls import path, include

from apps.auth import views

urlpatterns = [
    path("auth/", include('apps.auth.urls')),

    path("", views.index, name='index'),
    path('tests/', include('apps.Tests.urls')),
    path('courses/', include('apps.Courses.urls')),

    path('profile/', include('apps.Profile.urls')),

    path("admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns.append(
        path("__debug__/", include("debug_toolbar.urls")),
    )
