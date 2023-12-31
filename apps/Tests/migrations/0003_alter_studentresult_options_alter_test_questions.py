# Generated by Django 4.2.2 on 2023-07-08 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestsApp', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentresult',
            options={'verbose_name': 'Результат студента', 'verbose_name_plural': 'Результаты студентов'},
        ),
        migrations.AlterField(
            model_name='test',
            name='questions',
            field=models.ManyToManyField(blank=True, related_name='+', to='TestsApp.question', verbose_name='Вопросы'),
        ),
    ]
