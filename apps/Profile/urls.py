from django.urls import path
from .views import UserProfileView, delete_group

urlpatterns = [
    path('', UserProfileView.as_view(), name='profile'),
    path('delete-group/<str:group_index>', delete_group, name='delete-group')
]