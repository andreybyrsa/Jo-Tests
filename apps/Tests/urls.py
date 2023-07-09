from django.urls import path
from .views import ViewTests, CreateTest

urlpatterns = [
    path("", ViewTests.as_view(), name="tests"),
    path("create-test/", CreateTest.as_view(), name="create-test"),
    path("change-test/", CreateTest.as_view(), name="change-test"),
    path("delete-test/", CreateTest.as_view(), name="delete-test"),
    path("tests/", CreateTest.as_view(), name="inspect-test"),
    path("change-test/", CreateTest.as_view(), name="change-test"),
    path("delete-test/", CreateTest.as_view(), name="delete-test"),
    path("inspect-course/", CreateTest.as_view(), name="inspect-course"),
    path("profile/", CreateTest.as_view(), name="create-course"),
]
