from django.shortcuts import redirect, render
from core.utils.mixins import HeaderMixin, InfoSidebarMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.contrib import messages

from apps.auth.models import Teacher, Student
from apps.Tests.models import StudentResult, Test
from .models import Course, Group, CourseTest

from .forms import CourseCreateForm

from uuid import uuid4


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
            teacher = Teacher.objects.get(user__id=current_user.id)
            return teacher.courses.all()
        student = Student.objects.get(user__id=current_user.id)
        
        return student.courses.all()


class CreateCourse(LoginRequiredMixin, HeaderMixin, View):
    """Создание курса - Teacher"""

    login_url = "/auth/"
    redirect_field_name = "courses"

    def get(self, request):
        current_user = request.user
        # if current_user.role != 'teacher':
        #     messages.error(request, 'Доступ запрещен')
        #     return redirect('profile')
        form = CourseCreateForm
        header_def = self.get_user_header()
        teacher = Teacher.objects.get(user__id=current_user.id)
        groups = teacher.groups.all()
        groups_info = list(group.get_group_info() for group in groups)
        tests = Test.objects.all()
        tests_info = list(test.get_test_info() for test in tests)
        context = dict(list({"form": form, 'groups_info': groups_info, 'tests_info': tests_info}.items()) + list(header_def.items()))

        return render(request, "Courses/CreateCoursePage.html", context)
    
    def post(self, request):
        current_user = request.user
        post = request.POST
        teacher = Teacher.objects.get(user__id=current_user.id)
        course = Course.objects.create(
            title = post['title'],
            description = post['description'],
            teacher = teacher,
            progress = 0,
            slug = 'course' + str(uuid4())
        )
        teacher.courses.add(course)

        for post_group in post['groups'].split(' '):
            if post_group == '':
                continue
            group = Group.objects.get(index=post_group)
            course.groups.add(group)
            students = group.students.all()
            for student in students:
                student.courses.add(course)

            
                
        
        for post_test in post['tests'].split(' '):
            if post_test == '':
                continue
            info_test = post_test.split('/')
            test = Test.objects.get(slug=info_test[0])
            course_test = CourseTest.objects.create(
                course = course,
                test = test,
                test_time = info_test[2],
                is_available = True if info_test[1] == 'true' else False,
            )
            course.tests.add(course_test)
        
        return redirect('courses')
            


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
