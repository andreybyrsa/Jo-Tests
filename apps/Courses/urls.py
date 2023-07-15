from django.urls import path
from .views import (
    ViewCourses,
    CreateCourse,
    delete_course,
    EditCourse,
    ViewTestsInCourse,
)

urlpatterns = [
    path("", ViewCourses.as_view(), name="courses"),
    path("<slug:course_slug>", ViewTestsInCourse.as_view(), name="inspect-course"),
    path("create_course/", CreateCourse.as_view(), name="create-course"),
    path(
        "change_course/<slug:course_slug>", EditCourse.as_view(), name="change-course"
    ),
    path("delete_course/<slug:course_slug>", delete_course, name="delete-course"),
]
