# Generated by Django 5.0.1 on 2024-01-16 02:11

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(default='', max_length=16, unique=True)),
                ('code', models.CharField(default=api.models.generate_unique_code, max_length=8, unique=True)),
                ('username', models.CharField(default='', max_length=16)),
                ('tag', models.CharField(max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
