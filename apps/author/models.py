from django.db import models
from django.contrib.auth.models import AbstractUser

class Author(AbstractUser):
    profile_picture = models.FileField(null=True, blank=True, max_length=500)
    tests = models.ManyToManyField('Test')
    role = models.CharField(default='author')

