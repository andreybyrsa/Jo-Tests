from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(AbstractUser):
    profile_picture = models.FileField(null=True, blank=True, max_length=500)
    role = models.CharField(default='teacher')
    courses = models.ManyToManyField('Course')
    groups = models.ManyToManyField('Group')

class Group(models.Model):
    groupname = models.CharField(max_length=127)
    teache = models.ForeingKey('Teacher')
    students = models.ManyToManyField('studentApp.Student')

class Course(models.Model):
    title = models.TextField(max_length=127, verbose_name='Название теста')
    description = models.TextField(max_length=255, verbose_name = 'Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    tests = models.ManyToMany('authorApp.Test')
    groups = models.ManyToMany('Group')
    progress = models.FloatField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title', 'time_update']
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'