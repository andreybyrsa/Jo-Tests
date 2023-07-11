from django.shortcuts import redirect, render
from core.utils.mixins import HeaderMixin, InfoSidebarMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View

from apps.auth.models import Teacher, Student
from apps.Tests.models import StudentResult, Test
from .models import Course

from .forms import CourseCreateForm


class ViewCourses(LoginRequiredMixin, HeaderMixin, InfoSidebarMixin, ListView):
    """Список курсов - Student, Teacher"""

    model = Course
    login_url = "/auth"
    template_name = "Courses/CoursesPage.html"
    context_object_name = "courses"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        json_courses = list(course.get_course_info() for course in context["courses"])
        header_def = self.get_user_header()
        sidebar_def = self.get_user_sidebar()

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
        student = Student.objects.get(user=current_user)
        return student.courses.all()


class CreateCourse(LoginRequiredMixin, HeaderMixin, View):
    """Создание курса - Teacher"""

    login_url = "/auth/"
    redirect_field_name = "courses"

    def get(self, request):
        current_user = request.user
        form = CourseCreateForm
        header_def = self.get_user_header()
        teacher = Teacher.objects.get(user__id=current_user.id)
        groups = teacher.groups.all()
        groups_info = list(group.get_group_info() for group in groups)
        tests = Test.objects.all()
        tests_info = list(test.get_test_info() for test in tests)
        context = dict(list({"form": form, 'groups_info': groups_info, 'tests_info': tests_info}.items()) + list(header_def.items()))

        return render(request, "Courses/CreateCoursePage.html", context)
    
    # def post(self, request):


def delete_course(request, course_slug):
    """Удаление курса - Teacher"""

    Course.objects.get(slug=course_slug).delete()
    return redirect("courses")


class ViewTestsInCourse(HeaderMixin, InfoSidebarMixin, DetailView):
    """Список тестов в курсе - Teacher, Student"""

    model = Course
    template_name = ""
    context_object_name = "course"
    slug_url_kwarg = "course_slug"

    def get_context_data(self, *, object_list=None, **kwargs):
        current_user = self.request.user
        header_def = self.get_user_header()
        context = super().get_context_data(**kwargs)

        if current_user.role == "student":
            tests = context["course"].tests.filter(is_available=True)
            json_tests = list(test.get_test_info() for test in tests)

            return dict(
                list({"tests": tests}.items())
                + list(header_def.items())
                + list({"json_tests": json_tests}.items())
            )

        if current_user.role == "teacher":
            tests = context["course"].tests.all()
            results = context["course"].groups.students.results.all()

            return dict(
                list({"tests": tests}.items())
                + list(header_def.items())
                + list({"results": results}.items())
            )
