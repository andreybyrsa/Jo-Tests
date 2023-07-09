from django.shortcuts import redirect, render
from core.utils.mixins import HeaderMixin, InfoSidebarMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from apps.auth.models import Teacher, Student
from .models import Course


class ViewCourses(LoginRequiredMixin, HeaderMixin, InfoSidebarMixin, ListView):
    """Список курсов - Student, Teacher"""

    model = Course
    login_url = "/auth"
    template_name = "Courses/CoursesPage.html"
    context_object_name = "courses"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        json_courses = list(test.get_course_info() for test in context["courses"])
        header_def = self.get_user_header()
        sidebar_def = self.get_user_sidebar(urls=context['courses'])

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

def create_course(self):
    return HttpResponse()

def delete_course(request, course_slug):
    Course.objects.get(slug=course_slug).delete()
    return redirect('courses')


#Отображение тестов в курсе(teacher, student)

# class ViewTestsInCourse(HeaderMixin, InfoSidebarMixin, DetailView):
#       model = Course
#       template_name = ''
#       slug_url_kwarg = 'course_slug'
#       context_object_name = ''
      
#       def get_context_data(self, *, object_list=None, **kwargs):
#             context = super().get_context_data(**kwargs)
#             header_def = self.get_user_header()
#             sidebar_def = self.get_user_info()
#             return dict(list(context.items()) + list(header_def.items()) + list(inf0_sidebar_def.items()))
       
#        course = Course.objects.get(slug=self.kwargs.get(slug_url_kwargs)
#        current_user = self.request.user
#        def get_queryset(self):
#               if current_user.role == ‘teacher’:
#                      return course.tests.all()
#               return course.tests.filter(‘is_available’=True)