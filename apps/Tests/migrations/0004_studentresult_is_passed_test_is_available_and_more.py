# Generated by Django 4.2.2 on 2023-07-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestsApp', '0003_alter_studentresult_options_alter_test_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentresult',
            name='is_passed',
            field=models.BooleanField(default=False, verbose_name='Пройден'),
        ),
        migrations.AddField(
            model_name='test',
            name='is_available',
            field=models.BooleanField(default=False, verbose_name='Доступен'),
        ),
        migrations.AlterField(
            model_name='studentresult',
            name='result',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_time',
            field=models.IntegerField(verbose_name='Время выполнения теста'),
        ),
    ]
