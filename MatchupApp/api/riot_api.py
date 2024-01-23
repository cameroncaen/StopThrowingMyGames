import requests

def GetUserInfo(username, tag, api_key):
    api_url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/" + username + "/" + tag + "?api_key=" + api_key
    resp = requests.get(api_url)
    player_info = resp.json()
    