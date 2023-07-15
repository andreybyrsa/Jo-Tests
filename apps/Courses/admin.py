from django.contrib import admin
from django.contrib.auth.models import Group as DefaultGroup
from .models import Group, Course, CourseTest


class GroupAdmin(admin.ModelAdmin):
    list_display = ("groupname", "teacher")
    filter_horizontal = ("students",)


class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "teacher")
    filter_horizontal = ("tests", "groups")


admin.site.unregister(DefaultGroup)

admin.site.register(Group, GroupAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseTest)
