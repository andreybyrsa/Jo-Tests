from django.db import models
from apps.auth.models import Teacher


class Group(models.Model):
    groupname = models.CharField(max_length=127)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField('userAuth.Student', verbose_name='Студенты', )

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