from django.shortcuts import render
from core.utils.mixins import HeaderMixin, InfoSidebarMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView

from apps.auth.models import Teacher, Student
from .models import Course


class ViewCourses(LoginRequiredMixin, HeaderMixin, InfoSidebarMixin, ListView):
    """Список курсов - Teacher, Student"""

    model = Course
    login_url = "/auth"
    template_name = "Courses/CoursesPage.html"
    context_object_name = "courses"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        json_courses = list(course.get_course_info() for course in context["courses"])
        header_def = self.get_user_header()
        sidebar_def = self.get_user_sidebar("test")

        return dict(
            list(context.items())
            + list(header_def.items())
            + list(sidebar_def.items())
            + list({"json_courses": json_courses}.items())
        )

    def get_queryset(self):
        current_user = self.request.user

        if current_user.role == "teacher":
            teacher = Teacher.objects.get(user=current_user)
            return teacher.courses.all()

        # student = Author.objects.get(user=current_user)
        # return author.tests.all()


def create_course(request):
    return True
