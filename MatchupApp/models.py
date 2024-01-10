from django.db import models

# Create your models here.

# Player class containing all of the basic information needed for ALL players in the lobby
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

# This class "promotes" a player class into a MainPlayer which will have additional stats to
# view as they will be for the user of the webpage and their specific matchup in game
class MainPlayer(Player):
    #Others important stats imported from riot database will be stored here
    forward = models.IntegerField()


# This class stores important blurbs (tags) generated from observations of matchup stats. They
# contain the player being mentioned, the text describing them, and the importance (weight) of 
# the blurb to determine where on the webpage/heierarchy of stats it should go
class Tag(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tag_text = models.CharField(max_length=100)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.tag_text