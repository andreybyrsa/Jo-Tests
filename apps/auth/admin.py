from django.contrib import admin

from .models import User, Author, Student, Teacher

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Student)
admin.site.register(Teacher)
