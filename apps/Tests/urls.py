from django.urls import path
from .views import ViewTests, test_create

urlpatterns = [
    path("", ViewTests.as_view(), name="tests"),
    path('create_test/', test_create, name='create_test'),
    path('profile/', test_create, name='profile'),
    path('change_test/', test_create, name='change-test'),
    path('delete_test/', test_create, name='delete-test'),
    path('courses/', test_create, name='inspect-course'),
    path('profile/', test_create, name='create-course'),
    path('tests/', test_create, name='inspect-test'),
    path('courses/', test_create, name='courses'),
]