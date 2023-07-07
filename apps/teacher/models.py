from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(AbstractUser):
    profile_picture = models.FileField(null=True, blank=True, max_length=500)
    role = models.CharField(default='teacher', max_length=50)
    courses = models.ManyToManyField('teacherApp.Course')
    groups = models.ManyToManyField('teacherApp.Group')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

class Group(models.Model):
    groupname = models.CharField(max_length=127)
    teache = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField('studentApp.Student')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

class Course(models.Model):
    title = models.TextField(max_length=127, verbose_name='Название теста')
    description = models.TextField(max_length=255, verbose_name = 'Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    tests = models.ManyToManyField('authorApp.Test')
    groups = models.ManyToManyField(Group)
    progress = models.FloatField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title', 'time_update']
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'