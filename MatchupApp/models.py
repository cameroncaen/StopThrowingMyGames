from django.db import models

# Create your models here.

class Player(models.Model):
    username = models.CharField(max_length=25)
    level = models.IntegerField(default=0)
    rank = models.CharField(max_length=15)
    division = models.IntegerField(default=4)
    champion = models.CharField(max_length=25)
    kills = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    vision = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class MainPlayer(Player):
    forward = models.IntegerField()

class Tag(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tag_text = models.CharField(max_length=100)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.tag_text