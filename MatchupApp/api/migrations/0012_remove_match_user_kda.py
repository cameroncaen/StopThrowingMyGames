# Generated by Django 5.0.1 on 2024-02-04 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_match_user_kda'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='user_kda',
        ),
    ]
