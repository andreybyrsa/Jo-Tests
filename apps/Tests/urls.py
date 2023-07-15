from django.urls import path
from .views import ViewTests, delete_test, CreateTest, EditTest

urlpatterns = [
    path("", ViewTests.as_view(), name="tests"),
    path("<slug:test_slug>", EditTest.as_view(), name="inspect-test"),
    path("create_test/", CreateTest.as_view(), name="create-test"),
    path("change_test/<slug:test_slug>", EditTest.as_view(), name="change-test"),
    path("delete_test/<slug:test_slug>", delete_test, name="delete-test"),
]
