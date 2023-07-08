from django.contrib import admin

from .models import Test, StudentResult, Question, Answer, Choice

admin.site.register(Test)
admin.site.register(StudentResult)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Choice)
