from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_auth, name="auth"),
    path("logout", views.user_logout, name="logout"),
]
