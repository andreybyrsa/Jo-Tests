from django.urls import path
from .views import ViewTests, test_create, delete_test

urlpatterns = [
    path("", ViewTests.as_view(), name="tests"),
    path("<slug:test_slug>", test_create, name="inspect-test"),
    path('change_test/<slug:test_slug>', test_create, name='change-test'),
    path('delete_test/<slug:test_slug>', delete_test, name='delete-test'),
    path("create_test/", test_create, name="create-test"),
]
