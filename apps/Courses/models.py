from django.db import models
from django.urls import reverse
from apps.auth.models import Teacher


class Group(models.Model):
    groupname = models.CharField(max_length=127)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField("userAuth.Student", verbose_name="Студенты", related_name='students')
    index = models.CharField(max_length=127, blank=True)

    def get_group_info(self):
        return {
            'groupname': self.groupname,
            'index': self.index,
        }

    def __str__(self):
        return self.groupname

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class CourseTest(models.Model):
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    test = models.ForeignKey("TestsApp.Test", on_delete=models.CASCADE)
    date_expired = models.DateTimeField(verbose_name="Дата окончания доступа")
    test_time = models.IntegerField(verbose_name="Время выполнения теста")
    is_available = models.BooleanField(default=False, verbose_name="Доступен")

    def __str__(self):
        return self.test

    class Meta:
        ordering = ["is_available"]
        verbose_name = "Тест в курсе"
        verbose_name_plural = "Тесты в курсе"


class Course(models.Model):
    title = models.TextField(max_length=127, verbose_name="Название курса")
    description = models.TextField(max_length=255, verbose_name="Описание")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    tests = models.ManyToManyField(CourseTest, related_name="courseTests")
    groups = models.ManyToManyField(Group)
    progress = models.FloatField()
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse("inspect-course", kwargs={"course_slug": self.slug})

    def get_course_info(self):
        return {
            "title": self.title,
            "description": self.description,
            "time_create": self.time_create,
            "time_update": self.time_update,
            "progress": self.progress,
            "slug": self.slug,
        }

    def __str__(self):
        return self.title

    class Meta:
        ordering = (
            "title",
            "time_update",
        )
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
