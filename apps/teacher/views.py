from typing import Any, Dict

from django.db.models.query import QuerySet

from django.shortcuts import render

from .models import Course

from django.views.generic import DetailView, ListView

from core.utils.mixins import *



#Отображение тестов в курсе(teacher, student)



class ViewCourses(HeaderMixin, InfoSidebarMixin, ListView):
    model = Course
    template_name = ''
    context_object_name = 'courses'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        header_def = self.get_user_header()
        sidebar_def = self.get_user_info()
        return dict(list(context.items()) + list(header_def.items()) + list(sidebar_def.items()))

    def get_queryset(self):
        current_user = self.request.user
        if current_user.role == 'teacher':
            return Course


class ViewTestsInCurse(HeaderMixin, InfoSidebarMixin, DetailView):
    model = Course
    template_name = ''
    slug_url_kwarg = 'course_slug'
    context_object_name = 'tests'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        header_def = self.get_user_header()
        sidebar_def = self.get_user_info()
        return dict(list(context.items()) + list(header_def.items()) + list(sidebar_def.items()))

    def get_queryset(self):
        current_user = self.request.user
        course = Course.objects.get(slug=self.kwargs['slug'])
        if current_user.role == 'teacher':
            return course.tests.all()
        return course.tests.filter(is_available=True)


