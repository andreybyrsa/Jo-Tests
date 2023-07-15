# Generated by Django 4.2.2 on 2023-07-14 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CoursesApp', '0007_remove_coursetest_date_expired'),
        ('TestsApp', '0009_studentresult_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentresult',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CoursesApp.group'),
        ),
    ]
