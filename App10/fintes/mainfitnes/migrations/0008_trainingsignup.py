# Generated by Django 5.2.1 on 2025-05-13 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainfitnes', '0007_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingSignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('training_type', models.CharField(max_length=20, verbose_name='Тип тренировки')),
                ('training_id', models.IntegerField(verbose_name='ID тренировки')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата записи')),
            ],
        ),
    ]
