from .riot_api import lookupAccount, lookupSummoner

def pullMatchData(puuid, role):
    ret_dict = {}

    #Stores general information that will be used for all players regardless of role
    AcctInfo = lookupAccount(puuid)
    SummInfo = lookupSummoner(puuid)
    ret_dict['username'] = AcctInfo['gameName']
    ret_dict['tagline'] = AcctInfo['tagLine']
    ret_dict['sumLvl'] = SummInfo['summonerLevel']
    ret_dict['role'] = role

    #ret_dict['stats']

    #Stores role specific data to be used to generate blurbs and role-specific stas
    #if role == 'TOP':
        
    return ret_dict
    