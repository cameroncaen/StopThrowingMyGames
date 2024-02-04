from django.db import models
import string, random

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Match.objects.filter(code=code).count() == 0:
            break

    return code
# Create your models here.
class Match(models.Model):
    host = models.CharField(max_length=16, default="", unique=True)
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True)

    username = models.CharField(max_length=16, default="")
    tag = models.CharField(max_length=5, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    
    # -------- User and UserOpponent Matchup fields -----------------------------
    #start of User's account/game information/stats
    user_sumLevel = models.CharField(max_length=8, default = 0)
    user_role = models.CharField(max_length=8, default = 5)
    user_kills = models.CharField(max_length=4, default = 0)
    user_deaths = models.CharField(max_length=4, default = 0)
    user_assists = models.CharField(max_length=4, default = 0)
    user_wardsPlaced = models.CharField(max_length=4, default = 0)
    user_wardsKilled = models.CharField(max_length=4, default = 0)
    user_VWBought = models.CharField(max_length=4, default = 0)
    user_KP = models.CharField(max_length=4, default = 0)
    user_GPM = models.CharField(max_length=4, default = 0)
    user_DPM = models.CharField(max_length=4, default = 0)
    
    #start of User's Opponent account inormation/stats
    opp_username = models.CharField(max_length=16, default="")
    opp_tag = models.CharField(max_length=5, default="")
    opp_sumLevel = models.CharField(max_length=8, default = 0)
    opp_role = models.CharField(max_length=8, default = 5)
    opp_kills = models.CharField(max_length=4, default = 0)
    opp_deaths = models.CharField(max_length=4, default = 0)
    opp_assists = models.CharField(max_length=4, default = 0)
    opp_wardsPlaced = models.CharField(max_length=4, default = 0)
    opp_wardsKilled = models.CharField(max_length=4, default = 0)
    opp_VWBought = models.CharField(max_length=4, default = 0)
    opp_KP = models.CharField(max_length=4, default = 0)
    opp_GPM = models.CharField(max_length=4, default = 0)
    opp_DPM = models.CharField(max_length=4, default = 0)

    # -------- Ally and enemy 1 Matchup fields ----------------------------------
    #start of Ally1's account inormation/stats
    ally1_username = models.CharField(max_length=16, default="")
    ally1_tag = models.CharField(max_length=5, default="")
    ally1_sumLevel = models.CharField(max_length=8, default = 0)
    ally1_role = models.CharField(max_length=8, default = 5)
    ally1_kills = models.CharField(max_length=4, default = 0)
    ally1_deaths = models.CharField(max_length=4, default = 0)
    ally1_assists = models.CharField(max_length=4, default = 0)
    ally1_wardsPlaced = models.CharField(max_length=4, default = 0)
    ally1_wardsKilled = models.CharField(max_length=4, default = 0)
    ally1_VWBought = models.CharField(max_length=4, default = 0)
    ally1_KP = models.CharField(max_length=4, default = 0)
    ally1_GPM = models.CharField(max_length=4, default = 0)
    ally1_DPM = models.CharField(max_length=4, default = 0)

    #start of Ally1's Opponent account inormation/stats
    enemy1_username = models.CharField(max_length=16, default="")
    enemy1_tag = models.CharField(max_length=5, default="")
    enemy1_sumLevel = models.CharField(max_length=8, default = 0)
    enemy1_role = models.CharField(max_length=8, default = 5)
    enemy1_kills = models.CharField(max_length=4, default = 0)
    enemy1_deaths = models.CharField(max_length=4, default = 0)
    enemy1_assists = models.CharField(max_length=4, default = 0)
    enemy1_wardsPlaced = models.CharField(max_length=4, default = 0)
    enemy1_wardsKilled = models.CharField(max_length=4, default = 0)
    enemy1_VWBought = models.CharField(max_length=4, default = 0)
    enemy1_KP = models.CharField(max_length=4, default = 0)
    enemy1_GPM = models.CharField(max_length=4, default = 0)
    enemy1_DPM = models.CharField(max_length=4, default = 0)

    # -------- Ally and enemy 2 Matchup fields ----------------------------------
    #start of Ally2's account inormation/stats
    ally2_username = models.CharField(max_length=16, default="")
    ally2_tag = models.CharField(max_length=5, default="")
    ally2_sumLevel = models.CharField(max_length=8, default = 0)
    ally2_role = models.CharField(max_length=8, default = 5)
    ally2_kills = models.CharField(max_length=4, default = 0)
    ally2_deaths = models.CharField(max_length=4, default = 0)
    ally2_assists = models.CharField(max_length=4, default = 0)
    ally2_wardsPlaced = models.CharField(max_length=4, default = 0)
    ally2_wardsKilled = models.CharField(max_length=4, default = 0)
    ally2_VWBought = models.CharField(max_length=4, default = 0)
    ally2_KP = models.CharField(max_length=4, default = 0)
    ally2_GPM = models.CharField(max_length=4, default = 0)
    ally2_DPM = models.CharField(max_length=4, default = 0)
    

    #start of Ally2's Opponent account inormation/stats
    enemy2_username = models.CharField(max_length=16, default="")
    enemy2_tag = models.CharField(max_length=5, default="")
    enemy2_sumLevel = models.CharField(max_length=8, default = 0)
    enemy2_role = models.CharField(max_length=8, default = 5)
    enemy2_kills = models.CharField(max_length=4, default = 0)
    enemy2_deaths = models.CharField(max_length=4, default = 0)
    enemy2_assists = models.CharField(max_length=4, default = 0)
    enemy2_wardsPlaced = models.CharField(max_length=4, default = 0)
    enemy2_wardsKilled = models.CharField(max_length=4, default = 0)
    enemy2_VWBought = models.CharField(max_length=4, default = 0)
    enemy2_KP = models.CharField(max_length=4, default = 0)
    enemy2_GPM = models.CharField(max_length=4, default = 0)
    enemy2_DPM = models.CharField(max_length=4, default = 0)

    

    # -------- Ally and enemy 3 Matchup fields ----------------------------------
    #start of Ally3's account inormation/stats
    ally3_username = models.CharField(max_length=16, default="")
    ally3_tag = models.CharField(max_length=5, default="")
    ally3_sumLevel = models.CharField(max_length=8, default = 0)
    ally3_role = models.CharField(max_length=8, default = 5)
    ally3_kills = models.CharField(max_length=4, default = 0)
    ally3_deaths = models.CharField(max_length=4, default = 0)
    ally3_assists = models.CharField(max_length=4, default = 0)
    ally3_wardsPlaced = models.CharField(max_length=4, default = 0)
    ally3_wardsKilled = models.CharField(max_length=4, default = 0)
    ally3_VWBought = models.CharField(max_length=4, default = 0)
    ally3_KP = models.CharField(max_length=4, default = 0)
    ally3_GPM = models.CharField(max_length=4, default = 0)
    ally3_DPM = models.CharField(max_length=4, default = 0)

    #start of Ally3's Opponent account inormation/stats
    enemy3_username = models.CharField(max_length=16, default="")
    enemy3_tag = models.CharField(max_length=5, default="")
    enemy3_sumLevel = models.CharField(max_length=8, default = 0)
    enemy3_role = models.CharField(max_length=8, default = 5)
    enemy3_kills = models.CharField(max_length=4, default = 0)
    enemy3_deaths = models.CharField(max_length=4, default = 0)
    enemy3_assists = models.CharField(max_length=4, default = 0)
    enemy3_wardsPlaced = models.CharField(max_length=4, default = 0)
    enemy3_wardsKilled = models.CharField(max_length=4, default = 0)
    enemy3_VWBought = models.CharField(max_length=4, default = 0)
    enemy3_KP = models.CharField(max_length=4, default = 0)
    enemy3_GPM = models.CharField(max_length=4, default = 0)
    enemy3_DPM = models.CharField(max_length=4, default = 0)


    # -------- Ally and enemy 4 Matchup fields ----------------------------------
    #start of Ally4's account inormation/stats
    ally4_username = models.CharField(max_length=16, default="")
    ally4_tag = models.CharField(max_length=5, default="")
    ally4_sumLevel = models.CharField(max_length=8, default = 0)
    ally4_role = models.CharField(max_length=8, default = 5)
    ally4_kills = models.CharField(max_length=4, default = 0)
    ally4_deaths = models.CharField(max_length=4, default = 0)
    ally4_assists = models.CharField(max_length=4, default = 0)
    ally4_wardsPlaced = models.CharField(max_length=4, default = 0)
    ally4_wardsKilled = models.CharField(max_length=4, default = 0)
    ally4_VWBought = models.CharField(max_length=4, default = 0)
    ally4_KP = models.CharField(max_length=4, default = 0)
    ally4_GPM = models.CharField(max_length=4, default = 0)
    ally4_DPM = models.CharField(max_length=4, default = 0)

    #start of Ally4's Opponent account inormation/stats
    enemy4_username = models.CharField(max_length=16, default="")
    enemy4_tag = models.CharField(max_length=5, default="")
    enemy4_sumLevel = models.CharField(max_length=8, default = 0)
    enemy4_role = models.CharField(max_length=8, default = 5)
    enemy4_kills = models.CharField(max_length=4, default = 0)
    enemy4_deaths = models.CharField(max_length=4, default = 0)
    enemy4_assists = models.CharField(max_length=4, default = 0)
    enemy4_wardsPlaced = models.CharField(max_length=4, default = 0)
    enemy4_wardsKilled = models.CharField(max_length=4, default = 0)
    enemy4_VWBought = models.CharField(max_length=4, default = 0)
    enemy4_KP = models.CharField(max_length=4, default = 0)
    enemy4_GPM = models.CharField(max_length=4, default = 0)
    enemy4_DPM = models.CharField(max_length=4, default = 0)

