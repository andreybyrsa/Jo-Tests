from django.contrib import admin
from .models import Test, StudentResult, Question, Answer, Choice


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    filter_horizontal = ("questions",)


@admin.register(StudentResult)
class StudentResultAdmin(admin.ModelAdmin):
    list_display = ("student", "test", "result")


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "test")
    filter_horizontal = ("answers",)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("answer", "question")


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("student", "question", "answer", "is_selected")