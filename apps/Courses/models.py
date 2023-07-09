from django.db import models
from apps.auth.models import Teacher


class Group(models.Model):
    groupname = models.CharField(max_length=127)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField("userAuth.Student", verbose_name="Студенты")

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Course(models.Model):
    title = models.TextField(max_length=127, verbose_name="Название курса")
    description = models.TextField(max_length=255, verbose_name="Описание")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    tests = models.ManyToManyField("TestsApp.Test")
    groups = models.ManyToManyField(Group)
    progress = models.FloatField()
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL")

    def get_course_info(self):
        return {
            "title": self.title,
            "description": self.description,
            "time_create": self.time_create,
            "time_update": self.time_update,
            "progress": self.progress,
        }

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title", "time_update"]
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
