# Generated by Django 4.2.2 on 2023-07-16 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TestsApp', '0010_alter_studentresult_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='student_result',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='TestsApp.studentresult'),
        ),
        migrations.AddField(
            model_name='studentresult',
            name='choises',
            field=models.ManyToManyField(to='TestsApp.choice'),
        ),
    ]
