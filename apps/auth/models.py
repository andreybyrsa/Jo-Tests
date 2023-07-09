from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class RoleType(models.TextChoices):
        student = "student"
        author = "author"
        teacher = "teacher"

    profile_picture = models.FileField(
        null=True, blank=True, max_length=500, verbose_name="Аватар"
    )
    role = models.CharField(
        choices=RoleType.choices,
        default="student",
        max_length=50,
        verbose_name="Роль",
    )
    slug = models.SlugField(
        max_length=255, db_index=True, verbose_name="URL", blank=True
    )
    groups = None

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tests = models.ManyToManyField(
        "TestsApp.Test", verbose_name="Тесты", related_name="+", blank=True
    )

    def __str__(self) -> str:
        return f"Автор {self.user}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField('CoursesApp.Course', verbose_name='Курсы студента', related_name='+', blank=True,)
    result_tests = models.ManyToManyField(
        "TestsApp.StudentResult",
        verbose_name="Результат теста",
        related_name="+",
        blank=True,
    )

    def __str__(self) -> str:
        return f"Студент {self.user}"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(
        "CoursesApp.Course", verbose_name="Курсы", related_name="+", blank=True
    )
    groups = models.ManyToManyField(
        "CoursesApp.Group", verbose_name="Группы", related_name="+", blank=True
    )

    def __str__(self) -> str:
        return f"Преподаватель {self.user}"

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
