# Generated by Django 5.0.1 on 2024-02-03 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_match_ally1_role_match_ally1_sumlevel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='ally1_assists',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='ally1_deaths',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='ally1_kills',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='ally2_assists',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='ally2_deaths',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='ally2_kills',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='ally3_assists',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='ally3_deaths',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='ally3_kills',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='ally4_assists',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='ally4_deaths',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='ally4_kills',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='enemy1_assists',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='enemy1_deaths',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='enemy1_kills',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='enemy2_assists',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='enemy2_deaths',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='enemy2_kills',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='enemy3_assists',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='enemy3_deaths',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='enemy3_kills',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='enemy4_assists',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='enemy4_deaths',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='enemy4_kills',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='host_assists',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='host_deaths',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='host_kills',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='opp_assists',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='opp_deaths',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='match',
            name='opp_kills',
            field=models.CharField(default=0, max_length=4),
        ),
    ]
