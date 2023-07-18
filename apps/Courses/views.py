from django.shortcuts import redirect, render
from django.db.models import F
from core.utils.mixins import HeaderMixin, InfoSidebarMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.contrib import messages

from core.utils.get_unique_slug import get_unique_slug
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
        current_user = self.request.user
        context = super().get_context_data(**kwargs)
        json_courses = list(course.get_course_info() for course in context["courses"])
        header_def = self.get_user_header()
        sidebar_def = self.get_user_sidebar()

        context["json_courses"] = json_courses

        if current_user.role == "teacher":
            max_courses_points = {}

            for course in context["courses"]:
                groups = course.groups.all()
                tests = course.tests.filter(is_available=True)

                student_counter = 0
                course_points = 0

                for group in groups:
                    student_counter += group.students.all().count()

                for test in tests:
                    course_points += test.get_test_in_course_info()["test"][
                        "max_result"
                    ]

                max_courses_points[f"{course.slug}"] = student_counter * course_points

            for course in json_courses:
                current_slug = course["slug"]
                course["max_course_progress"] = max_courses_points[current_slug]

        elif current_user.role == "student":
            # student = Student.objects.get(user__id=current_user.id)
            max_course_points = {}

            for course in context["courses"]:
                course_test = course.tests.filter(is_available=True)

                course_points = 0
                for test in course_test:
                    course_points += test.get_test_in_course_info()["test"][
                        "max_result"
                    ]

                max_course_points[f"{course.slug}"] = course_points

            for course in json_courses:
                current_slug = course["slug"]
                course["max_course_progress"] = max_course_points[current_slug]

            #     course_progress[f"{course.slug}"] = list()

            #     results_count = student.result_tests.filter(
            #         course__slug=course.slug
            #     ).count()
            #     course_progress[f"{course.slug}"].append(results_count)

            #     tests_count = course.tests.filter(is_available=True).count()
            #     course_progress[f"{course.slug}"].append(tests_count)

            # context["course_progress"] = course_progress

        return dict(
            list(context.items()) + list(header_def.items()) + list(sidebar_def.items())
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
        if current_user.role != "teacher":
            messages.error(request, "Доступ запрещен")
            return redirect("profile")
        form = CourseCreateForm
        header_def = self.get_user_header()
        teacher = Teacher.objects.get(user__id=current_user.id)
        groups = teacher.groups.all()
        groups_info = list(group.get_group_info() for group in groups)
        tests = Test.objects.all()
        tests_info = list(test.get_test_info() for test in tests)
        context = dict(
            list(
                {
                    "form": form,
                    "groups_info": groups_info,
                    "tests_info": tests_info,
                }.items()
            )
            + list(header_def.items())
        )

        return render(request, "Courses/CreateCoursePage.html", context)

    def post(self, request):
        current_user = request.user
        post = request.POST
        teacher = Teacher.objects.get(user__id=current_user.id)
        try:
            course = Course.objects.create(
                title=post["title"],
                description=post["description"],
                teacher=teacher,
                progress=0,
                slug=get_unique_slug(Course, post["title"]),
            )
            teacher.courses.add(course)

            for post_group in post["groups"].split(" "):
                if post_group == "":
                    continue
                group = Group.objects.get(index=post_group)
                course.groups.add(group)
                students = group.students.all()
                for student in students:
                    student.courses.add(course)

            for post_test in post["tests"].split(" "):
                if post_test == "":
                    continue
                info_test = post_test.split("/")
                test = Test.objects.get(slug=info_test[0])
                course_test = CourseTest.objects.create(
                    course=course,
                    test=test,
                    test_time=info_test[2],
                    is_available=True if info_test[1] == "true" else False,
                )
                course.tests.add(course_test)
            messages.success(request, "Курс успешно создан")
            return redirect("courses")

        except:
            messages.error(request, "Ошибка создания курса")
            return redirect("courses")


class EditCourse(LoginRequiredMixin, HeaderMixin, View):
    """Редактирование курса - Teacher"""

    login_url = "/auth/"
    redirect_field_name = "courses"

    def get(self, request, course_slug):
        current_user = request.user
        if current_user.role != "teacher":
            messages.error(request, "Доступ запрещен")
            return redirect("profile")

        form = CourseCreateForm
        header_def = self.get_user_header()
        teacher = Teacher.objects.get(user__id=current_user.id)
        groups = teacher.groups.all()
        groups_info = list(group.get_group_info() for group in groups)
        tests = Test.objects.all()
        tests_info = list(test.get_test_info() for test in tests)
        course = Course.objects.get(slug=course_slug)
        course_tests = course.tests.all()
        course_tests_info = [test.get_test_in_course_info() for test in course_tests]
        course_groups = course.groups.all()
        course_groups_info = [group.get_group_info() for group in course_groups]
        context = dict(
            list(
                {
                    "form": form,
                    "course": course.get_course_info(),
                    "groups_info": groups_info,
                    "tests_info": tests_info,
                    "course_tests_info": course_tests_info,
                    "course_groups_info": course_groups_info,
                }.items()
            )
            + list(header_def.items())
        )

        return render(request, "Courses/CreateCoursePage.html", context)

    def post(self, request, course_slug):
        current_user = request.user
        post = request.POST
        course = Course.objects.get(slug=course_slug)

        try:
            course.title = post["title"]
            course.description = post["description"]

            course.tests.clear()
            CourseTest.objects.filter(course__id=course.id).delete()
            groups = course.groups.all()
            for group in groups:
                for student in group.students.all():
                    student.courses.remove(course)
            course.groups.clear()
            course.progress = 0

            for post_group in post["groups"].split(" "):
                if post_group == "":
                    continue
                group = Group.objects.get(index=post_group)
                course.groups.add(group)
                students = group.students.all()
                for student in students:
                    student.courses.add(course)

            course_progress = 0
            for post_test in post["tests"].split(" "):
                if post_test == "":
                    continue
                info_test = post_test.split("/")
                test = Test.objects.get(slug=info_test[0])
                course_test = CourseTest.objects.create(
                    course=course,
                    test=test,
                    test_time=info_test[2],
                    is_available=True if info_test[1] == "true" else False,
                )
                course.tests.add(course_test)

                if course_test.is_available:
                    current_student_result = StudentResult.objects.filter(
                        course__slug=course.slug, test=course_test.test
                    )

                    tests_results = 0
                    for result in current_student_result:
                        tests_results += result.get_result_info()["result"]

                    course_progress += tests_results
                
            course.progress = course_progress

            course.save()
            messages.success(request, "Курс успешно изменён")
            return redirect("courses")

        except:
            messages.error(request, "Ошибка изменения курса")
            return redirect("courses")


def delete_course(request, course_slug):
    """Удаление курса - Teacher"""

    Course.objects.get(slug=course_slug).delete()
    return redirect("courses")


class ViewTestsInCourse(HeaderMixin, InfoSidebarMixin, DetailView):
    """Список тестов в курсе - Teacher, Student"""

    model = Course
    template_name = "Courses/CourseTestsPage.html"
    context_object_name = "course"
    slug_url_kwarg = "course_slug"

    def get_context_data(self, *, object_list=None, **kwargs):
        current_user = self.request.user
        header_def = self.get_user_header()
        context = super().get_context_data(**kwargs)

        if current_user.role == "student":
            course_tests = context["course"].tests.filter(is_available=True)
            json_course_tests = list(
                test.get_test_in_course_info() for test in course_tests
            )

            course_results = []
            student = Student.objects.get(user__id=current_user.id)

            for course_test in json_course_tests:
                test = Test.objects.get(slug=course_test["test"]["slug"])
                if StudentResult.objects.filter(
                    student=student,
                    test__id=test.id,
                    course__slug=context["course"].slug,
                ).exists():
                    result = StudentResult.objects.get(
                        student=student,
                        test__id=test.id,
                        course__slug=context["course"].slug,
                    )
                    course_results.append(result.get_result_info())

            return dict(
                list(header_def.items())
                + list(
                    {
                        "json_user": current_user.get_user_info(),
                        "json_course_tests": json_course_tests,
                        "tests_results": course_results,
                    }.items()
                )
            )

        elif current_user.role == "teacher":
            course_tests = context["course"].tests.all()
            groups = context["course"].groups.all()
            json_groups = {}
            json_course_tests = []

            for course_test in course_tests:
                json_course_tests.append(course_test.get_test_in_course_info())
                json_groups[
                    f"{course_test.get_test_in_course_info()['test']['slug']}"
                ] = list(
                    group.get_group_info(
                        test_slug=course_test.get_test_in_course_info()["test"]["slug"],
                        course_slug=context["course"].slug,
                    )
                    for group in groups
                )

            return dict(
                list(header_def.items())
                + list(
                    {
                        "json_course_tests": json_course_tests,
                        "groups": groups,
                        "json_groups": json_groups,
                    }.items()
                )
            )
