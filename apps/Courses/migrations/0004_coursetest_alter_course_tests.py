# Generated by Django 4.2.2 on 2023-07-10 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TestsApp', '0005_remove_test_date_expired_remove_test_is_available_and_more'),
        ('CoursesApp', '0003_alter_course_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_expired', models.DateTimeField(verbose_name='Дата окончания доступа')),
                ('test_time', models.IntegerField(verbose_name='Время выполнения теста')),
                ('is_available', models.BooleanField(default=False, verbose_name='Доступен')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CoursesApp.course')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestsApp.test')),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='tests',
            field=models.ManyToManyField(related_name='courseTests', to='CoursesApp.coursetest'),
        ),
    ]
