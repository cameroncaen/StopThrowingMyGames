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
    if user == 0:
        AcctInfo = lookupAccount(puuid)
        SummInfo = lookupSummoner(puuid)
        ret_dict['username'] = AcctInfo['gameName']
        ret_dict['tagline'] = AcctInfo['tagLine']
        ret_dict['sumLvl'] = SummInfo['summonerLevel']
        ret_dict['role'] = role

    ret_dict['stats'] = {
        'kills': 0,
        'deaths': 0,
        'assists': 0
    }
    stats = ret_dict['stats']

    #Stores role specific data to be used to generate blurbs and role-specific stas
    #if role == 'TOP':
    gameData = {}
    matches = MatchHistory(puuid)
    numGames = len(matches)
    for match_id in matches:
        match = MatchData(match_id)
        participants = match['info']['participants']
        for participant in participants:
            if participant['puuid'] == puuid:
                player = participant
        stats['kills'] += round(Decimal(player['kills'] / numGames), 1)
        stats['deaths'] += round(Decimal(player['deaths'] / numGames), 1)
        stats['assists'] += round(Decimal(player['assists'] / numGames), 1)

    if user == 0:
        return ret_dict
    else:
        return ret_dict['stats']
    