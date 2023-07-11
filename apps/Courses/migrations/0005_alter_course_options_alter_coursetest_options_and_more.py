# Generated by Django 4.2.2 on 2023-07-11 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0002_student_courses'),
        ('CoursesApp', '0004_coursetest_alter_course_tests'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('title', 'time_update'), 'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AlterModelOptions(
            name='coursetest',
            options={'ordering': ['is_available'], 'verbose_name': 'Тест в курсе', 'verbose_name_plural': 'Тесты в курсе'},
        ),
        migrations.AlterField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(related_name='students', to='userAuth.student', verbose_name='Студенты'),
        ),
    ]