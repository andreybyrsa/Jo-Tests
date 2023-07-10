from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class RoleType(models.TextChoices):
        STUDENT = "student"
        AUTHOR = "author"
        TEACHER = "teacher"

    profile_picture = models.FileField(
        null=True, blank=True, verbose_name="Аватар"
    )
    role = models.CharField(
        choices=RoleType.choices,
        default=RoleType.STUDENT,
        max_length=50,
        verbose_name="Роль",
    )
    slug = models.SlugField(
        max_length=255, db_index=True, blank=True, verbose_name="URL"
    )


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    tests = models.ManyToManyField(
        "TestsApp.Test", verbose_name="Тесты", related_name="authors", blank=True
    )

    def __str__(self):
        return f"Автор {self.user}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    courses = models.ManyToManyField(
        "CoursesApp.Course",
        verbose_name="Курсы студента",
        related_name="students",
        blank=True,
        help_text="Select the courses for the student.",
    )
    result_tests = models.ManyToManyField(
        "TestsApp.StudentResult",
        verbose_name="Результаты тестов",
        related_name="students",
        blank=True,
    )

    def __str__(self):
        return f"Студент {self.user}"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    courses = models.ManyToManyField(
        "CoursesApp.Course",
        verbose_name="Курсы",
        related_name="teachers",
        blank=True,
    )
    groups = models.ManyToManyField(
        "CoursesApp.Group",
        verbose_name="Группы",
        related_name="teachers",
        blank=True,
    )

    def __str__(self):
        return f"Преподаватель {self.user}"