from django.contrib import admin
from .models import User, Author, Student, Teacher


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ("User info", {"fields": ["username", "first_name", "last_name", "password"]}),
        ("User data", {"fields": ["profile_picture"]}),
    ]


class AuthorAdmin(admin.ModelAdmin):
    filter_horizontal = ("tests",)


class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ("courses", "result_tests")


class TeacherAdmin(admin.ModelAdmin):
    filter_horizontal = ("courses", "groups")


admin.site.register(User, UserAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)