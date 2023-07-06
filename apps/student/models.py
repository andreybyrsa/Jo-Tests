from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):
    profile_picture = models.FileField(null=True, blank=True, max_length=500)
    role = models.CharField(default='student')

    def __str__(self):
        return self.username



