# Generated by Django 5.2.1 on 2025-05-13 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainfitnes', '0008_trainingsignup'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallbackRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
