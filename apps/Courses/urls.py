from django.urls import path
from .views import ViewCourses, create_course, delete_course

urlpatterns = [
    path("", ViewCourses.as_view(), name="courses"),
    path("create_course/", create_course, name="create-course"),
    path("change_test/", create_course, name="change-course"),
    path("delete_test/<slug:course_slug>", delete_course, name="delete-course"),
    path("<slug:course_slug>", create_course, name="inspect-course"),
]
