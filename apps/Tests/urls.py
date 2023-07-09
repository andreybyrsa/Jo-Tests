from django.urls import path
from .views import ViewTests, test_create

urlpatterns = [
    path("", ViewTests.as_view(), name="tests"),
    path("create-test/", test_create, name="create-test"),
    path("change-test/", test_create, name="change-test"),
    path("delete-test/", test_create, name="delete-test"),
    path("tests/", test_create, name="inspect-test"),
    path('change-test/', test_create, name='change-test'),
    path('delete-test/', test_create, name='delete-test'),
    path('inspect-course/', test_create, name='inspect-course'),
    path('profile/', test_create, name='create-course'),
]
