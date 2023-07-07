from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):
    profile_picture = models.FileField(null=True, blank=True, max_length=500)
    role = models.CharField(default='student')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.username

class StudentResult(models.Model):
    student = models.ForeignKey('Student', on_delete = models.CASCADE)
    test = models.ForeignKey('authorApp.Test', on_delete = models.CASCADE)
    result = models.FloatField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')



class Choice(models.Model):
    question = models.ForeignKey('authorApp.Question', on_delete = models.CASCADE)
    student = models.ForeignKey('Student', on_delete = models.CASCADE)
    answer = models.ForeignKey('authorApp.Answer', on_delete = models.CASCADE)
    is_selected = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')