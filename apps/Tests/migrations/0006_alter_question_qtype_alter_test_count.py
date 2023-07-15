# Generated by Django 4.2.2 on 2023-07-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestsApp', '0005_remove_test_date_expired_remove_test_is_available_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='qtype',
            field=models.CharField(choices=[('single', 'Single'), ('multiple', 'Multiple')], default='single', max_length=8),
        ),
        migrations.AlterField(
            model_name='test',
            name='count',
            field=models.PositiveIntegerField(verbose_name='Количество вопросов'),
        ),
    ]
