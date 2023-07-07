from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class RoleType(models.TextChoices):
        student = "student"
        author = "author"
        teacher = "teacher"

    profile_picture = models.FileField(
        null=True, blank=True, max_length=500, verbose_name=("Аватар")
    )
    role = models.CharField(
        choices=RoleType.choices,
        default="student",
        max_length=50,
        verbose_name=("Роль"),
    )
    slug = models.SlugField(
        max_length=255, db_index=True, verbose_name=("URL"), blank=True
    )
    groups = None


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tests = models.ManyToManyField(
        "authorApp.Test", verbose_name="Тесты", related_name="+"
    )


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result_tests = models.ManyToManyField(
        "studentApp.StudentResult", verbose_name=("Результат теста"), related_name="+"
    )


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(
        "teacherApp.Course", verbose_name=("Курсы"), related_name="+"
    )
    groups = models.ManyToManyField(
        "teacherApp.Group", verbose_name=("Группы"), related_name="+"
    )
