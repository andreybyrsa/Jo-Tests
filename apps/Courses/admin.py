from django.contrib import admin
from django.contrib.auth.models import Group as DefaultGroup

from .models import Group, Course, CourseTest

admin.site.unregister(DefaultGroup)

admin.site.register(Group)
admin.site.register(Course) 
admin.site.register(CourseTest)
