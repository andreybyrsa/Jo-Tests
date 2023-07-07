from django.contrib import admin

from .models import User, Author, Student, Teacher
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.register(User)
admin.site.register(Author)
admin.site.register(Student)
admin.site.register(Teacher)

