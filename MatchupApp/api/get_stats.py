from .riot_api import lookupAccount, lookupSummoner, MatchHistory, MatchData
from decimal import Decimal

# For user param:
#   0 is a player in an alternate role/lane than the user
#   1 is the user's role/lane opponent
#   2 is the user
# This distinction is used to make less arbitrary dictionary element accesses
def pullMatchData(puuid, role, champ, user):
    ret_dict = {}

    #Stores general information that will be used for all players regardless of role
    if user != 2:
        ret_dict['username'] = ""
        ret_dict['tagline'] = ""
        ret_dict['sumLvl'] = ""
        ret_dict['role'] = role

    ret_dict['stats'] = {
        'kills': 0,
        'deaths': 0,
        'assists': 0,
        'OTP': 0,
        'inRole': 0,
        'wardsPlaced': 0,
        'wardsKilled': 0,
        'visionWardsBoughtInGame': 0,
        'GPM': 0,
        'DPM': 0,
        'KP': 0,

        # ChampSpecifc stats are defined below this line, not all may be used per role
        # These will be used in blurb generation
        'SSD': 0,
        'soloKills': 0,
        'buffsStolen': 0,
        'questOT': 0,
        
        'enemyJungleMonsterKills': 0,
        'jgEarlyKills': 0,
        'firstTurret': 0,
        'turretPlates': 0,
        'saveAllyFromDeath': 0,
        'landSS': 0,
        'csADV': 0
        


    }
    stats = ret_dict['stats']

    #Stores role specific data to be used to generate blurbs and role-specific stas
    #if role == 'TOP':
    matches = MatchHistory(puuid)
    numGames = len(matches)
    if user != 2 and numGames == 0:
        acct = lookupAccount(puuid)
        sum = lookupSummoner(puuid)
        ret_dict['username'] = acct['gameName']
        ret_dict['tagline'] = acct['tagLine']
        ret_dict['sumLvl'] = sum['summonerLevel']
    count = 0
    countInRole = 1
    for match_id in matches:
        match = MatchData(match_id)
        participants = match['info']['participants']
        for participant in participants:
            if participant['puuid'] == puuid:
                player = participant
        if user  != 2 and count == 0:
            ret_dict['username'] = player['riotIdGameName']
            ret_dict['tagline'] = player['riotIdTagline']
            ret_dict['sumLvl'] = player['summonerLevel']
            count += 1
        chals = player['challenges']
        stats['kills'] += round(Decimal(player['kills'] / numGames), 1)
        stats['deaths'] += round(Decimal(player['deaths'] / numGames), 1)
        stats['assists'] += round(Decimal(player['assists'] / numGames), 1)
        stats['wardsPlaced'] += round(Decimal(player['wardsPlaced'] / numGames), 1)
        stats['wardsKilled'] += round(Decimal(player['wardsKilled'] / numGames), 1)
        stats['visionWardsBoughtInGame'] += round(Decimal(player['visionWardsBoughtInGame'] / numGames), 1)
        stats['KP'] += round(Decimal(chals['killParticipation'] / numGames), 2)
        stats['GPM'] += round(Decimal(chals['goldPerMinute'] / numGames), 2)
        stats['DPM'] += round(Decimal(chals['damagePerMinute'] / numGames), 2)

        # Checks if player plays their champ a lot
        if user != 0 and player['championId'] == champ:
            stats['OTP'] += 1


        if player['teamPosition'] == role:
            stats['inRole'] += 1
            stats['SSD'] += round(Decimal(chals['skillshotsDodged'] / countInRole), 1)
            
            if role == 'TOP':
                stats['soloKills'] += round(Decimal(chals['soloKills'] / countInRole), 1)
                stats['firstTurret'] += round(Decimal(chals['firstTurretKilled'] / countInRole), 1)
                stats['turretPlates'] += round(Decimal(chals['turretPlatesTaken'] / countInRole), 1)
                stats['csADV'] += round(Decimal(chals['maxCsAdvantageOnLaneOpponent'] / countInRole), 1)

                
            elif role == 'JUNGLE':
                stats['buffsStolen'] += round(Decimal(chals['buffsStolen'] / countInRole), 1)
                stats['enemyJungleMonsterKills'] += round(Decimal(chals['enemyJungleMonsterKills'] / countInRole), 1)
                stats['jgEarlyKills'] += round(Decimal(chals['junglerKillsEarlyJungle'] / countInRole), 1)
                stats['csADV'] += round(Decimal(chals['maxCsAdvantageOnLaneOpponent'] / countInRole), 1)

                
            elif role == 'MIDDLE':
                stats['soloKills'] += round(Decimal(chals['soloKills'] / countInRole), 1)
                stats['firstTurret'] += round(Decimal(chals['firstTurretKilled'] / countInRole), 1)
                stats['turretPlates'] += round(Decimal(chals['turretPlatesTaken'] / countInRole), 1)
                stats['csADV'] += round(Decimal(chals['maxCsAdvantageOnLaneOpponent'] / countInRole), 1)

            elif role == 'BOTTOM':
                stats['soloKills'] += round(Decimal(chals['soloKills'] / countInRole), 1)
                stats['firstTurret'] += round(Decimal(chals['firstTurretKilled'] / countInRole), 1)
                stats['turretPlates'] += round(Decimal(chals['turretPlatesTaken'] / countInRole), 1)
                stats['csADV'] += round(Decimal(chals['maxCsAdvantageOnLaneOpponent'] / countInRole), 1)


            else:
                if chals['completeSupportQuestInTime'] == True:
                    stats['questOT'] += 1
                stats['saveAllyFromDeath'] += round(Decimal(chals['saveAllyFromDeath'] / countInRole), 1)
                stats['landSS'] += round(Decimal(chals['landSkillShotsEarlyGame'] / countInRole), 1)
                
            countInRole += 1
    if user != 2:
        return ret_dict
    else:
        return ret_dict['stats']
    