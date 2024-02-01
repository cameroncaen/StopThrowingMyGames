import requests
from .user_info import user_RiotKey

riotKey = user_RiotKey()

# Takes the username, the riot tag, and the user's api_key in order to get the puuid for the other Riot APIs and the id in order to check whether the user is currently in a game
def GetUserInfo(username, tag):
    api_url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/" + username + "/" + tag + "?api_key=" + riotKey
    resp = requests.get(api_url)
    user_info = resp.json()
    # Gets the puuid in order to be able to get more info about the summoner
    user_puuid = str(user_info['puuid'])
    summoner_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/" + user_puuid + "?api_key=" + riotKey
    resp2 = requests.get(summoner_url)
    more_player_info = resp2.json()
    # Gets the id in order to check whether the user is currently in a match
    return more_player_info
    
# Takes the user_id and finds out if they are in a live match and gets the puuid of the other players
def GetInfoFromLiveMatch(user_id):
    live_match_url = "https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + user_id + "?api_key=" + riotKey
    resp = requests.get(live_match_url)
    match_info = resp.json()
    
    # Gets the puuid of all the players in the game
    players_puuid = match_info['participants']
    return players_puuid

# Takes in a puuid and gets the associated Account
def lookupAccount(puuid):
    account_lookup_url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-puuid/" + puuid + "?api_key=" + riotKey
    resp = requests.get(account_lookup_url)
    account_info = resp.json()
    return account_info

# Takes in a puuid and gets the associated Summoner
def lookupSummoner(puuid):
    summoner_lookup_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/" + puuid + "?api_key=" + riotKey
    resp = requests.get(summoner_lookup_url)
    summoner_info = resp.json()
    return summoner_info

# Takes in a puuid and gets the user's match history
def MatchHistory(puuid):
    match_history_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?start=0&count=5" + "&api_key=" + riotKey
    resp = requests.get(match_history_url)
    match_list = resp.json()
    return match_list

# Takes in a match ID and gets data about the match
def MatchData(match_id):
    match_url = "https://americas.api.riotgames.com/lol/match/v5/matches/" + match_id + "?api_key=" + riotKey
    resp = requests.get(match_url)
    match_data = resp.json()
    return match_data

    # NOTEWORTHY STATS
        # LITERAL STATS
            
        # INFERRED STATS
            #['firstTurretKill']