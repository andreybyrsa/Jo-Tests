from django.urls import path
from .views import ViewTests, test_create

urlpatterns = [
    path("", ViewTests.as_view(), name="tests"),
    path("create_test/", test_create, name="create-test"),
    path("change_test/", test_create, name="change-test"),
    path("delete_test/", test_create, name="delete-test"),
    path("tests/", test_create, name="inspect-test"),
]
