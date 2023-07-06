from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(AbstractUser):
    profile_picture = models.FileField(null=True, blank=True, max_length=500)
    role = models.CharField(default='teacher')
    courses = models.ManyToManyField('Course')
    groups = models.ManyToManyField('Group')