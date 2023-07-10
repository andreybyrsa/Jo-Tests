from django.contrib import admin
from django.contrib.auth.models import Group as DefaultGroup
from .models import Group, Course

admin.site.unregister(DefaultGroup)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("groupname", "teacher")
    filter_horizontal = ("students",)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "teacher")
    filter_horizontal = ("tests", "groups")