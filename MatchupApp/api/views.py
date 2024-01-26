from django.shortcuts import render
from rest_framework import generics, status
from .serializers import MatchSerializer, PopulateMatchupInfoSerializer
from .riot_api import GetUserInfo, GetInfoFromLiveMatch, lookupAccount, lookupSummoner
from .models import Match
from rest_framework.views import APIView
from rest_framework.response import Response
from roleidentification import pull_data, get_roles

# Create your views here.
# using .ListApiView is for seeing the views rather than generating them
# REACT ALLOWS FOR THE CODE TO GENERATE THESE RATHER THAN THE UI ON THE BROWSER CURRENTLY
class MatchView(generics.ListAPIView):
    # What do we want to return?
    queryset = Match.objects.all()
    # How do I convert these Match objects into a readable/usable format?
    serializer_class = MatchSerializer

#class populateMatchupInfo(APIView)
    #grabbing user data from riot API
    #using that to access match for players ( or manual input other players)
    #grab other player data
    #populate models with respective information
    #export models to matchup webpage
    #jump to webpage (handled outside this file)


class GetMatchInfo(APIView):
    serializer_class = MatchSerializer
    lookup_url_kwarg = 'code'

    def get(self, request, format=None):
        code = request.GET.get(self.lookup_url_kwarg)
        if code is None:
            return Response({'Bad Request': 'Code paramater not found in request'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            match = Match.objects.get(code=code)
            if match:
                data = MatchSerializer(match).data
                return Response(data, status.HTTP_200_OK)
            else:
                return Response({'Match Not Found': 'Invalid match Code.'}, status=status.HTTP_404_NOT_FOUND)
        except Match.DoesNotExist:
            return Response({'Match Not Found': 'Invalid match Code.'}, status=status.HTTP_404_NOT_FOUND)

#Fetches roles for each player and returns a dictionary of 2 nested dictionaires with the role and champId 
#mapped to a player's summonerId
def findRoles(players, id):
    roles = {}
    your_team = {}
    enemy_team = {}
    champion_roles = pull_data()
    team1_champions = [players[0]['championId'], 
                      players[1]['championId'], 
                      players[2]['championId'], 
                      players[3]['championId'], 
                      players[4]['championId']]
    team2_champions = [players[5]['championId'], 
                      players[6]['championId'], 
                      players[7]['championId'], 
                      players[8]['championId'], 
                      players[9]['championId']]
    your_roles = get_roles(champion_roles, team1_champions)
    enemy_roles = get_roles(champion_roles, team2_champions)
    print(your_roles)
    print(enemy_roles)
    for x in range(5):
        champ =  players[x]['championId']   
        for role in your_roles:
            if your_roles[role] == champ:
                your_team[players[x]["puuid"]] = {'role': (role), 'champId': champ, 'number': x}
    roles['team1'] = your_team
    for x in range(5):
        champ = players[x+5]['championId']   
        for role in enemy_roles:
            if enemy_roles[role] == champ:
                enemy_team[players[x+5]["puuid"]] = {'role': (role), 'champId': champ, 'number': x+5}
    roles['team2'] = enemy_team
    return roles


def generateInfo(username, tag):
    userData = GetUserInfo(username, tag)
    players = GetInfoFromLiveMatch(str(userData["id"]))
    #-------Match Fetched at this point and returned as list of player dictionaries----------
    roles = findRoles(players, str(userData["id"]))
    print(roles)
    ally = ''
    enemy = ''
    temp = 0
    if (userData["puuid"]) in (roles['team1']):
        ally = 'team1'
        enemy = 'team2'
        temp = 5
    else :
        ally = 'team2'
        enemy = 'team1'
    userRole = roles[ally][userData["puuid"]]['role']

    #------Roles are determined with the git import and User's team is declared from list of players----
    #------team1 refers to players[0-4] and team2 refers to players[5-9]--------------------------------
    userOpp = ''
    oppPuuid= ''
    for key in roles[enemy]:
        if roles[enemy][key]['role'] == userRole:
            oppPuuid = key
            print("WORKS")
            break
    oppNum = roles[enemy][oppPuuid]['number']
    #-----------Lookup User Opponent to populate stats -------------------------------------------------
    OppAcct = lookupAccount(oppPuuid)
    OppSumm = lookupSummoner(oppPuuid)
    #------Nested Dictionaries under lebel allMatchData are declared to be updated below ---------------
    allMatchData = {
        "User": {
            "sumLvl": userData['summonerLevel'],
            "role" : userRole
        },
        "UserOpp": {
            'username': OppAcct['gameName'],
            'tagline': OppAcct['tagLine'],
            "sumLvl": OppSumm['summonerLevel'],
            "role" : roles[enemy][oppPuuid]['role']
        },
        "AltLane1": {

        },
        "AltLaneOpp1": {

        },
        "AltLane2": {

        },
        "AltLaneOpp2": {

        },
        "AltLane3": {

        },
        "AltLaneOpp3": {

        },
        "AltLane4": {

        },
        "AltLaneOpp4": {

        }
    }
        
    return allMatchData

class PopulateMatchupInfo(APIView):
    serializer_class = PopulateMatchupInfoSerializer
     
    

    def post(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            tag = serializer.data.get('tag')
            host = self.request.session.session_key
            queryset = Match.objects.filter(host = host)
            if queryset.exists():
                match = queryset[0]
                match.username = username
                match.tag = tag
                match.save(update_fields=['username', 'tag'])
                #Beginning of generating stats------------------------------
                matchInfo = generateInfo(username, tag)
                #user Model Fields
                match.user_sumLevel = matchInfo['User']['sumLvl']
                match.user_role = matchInfo['User']['role']
                match.save(update_fields=['user_sumLevel', 'user_role'])
                #Opp Model Fields
                match.opp_username = matchInfo['UserOpp']['username']
                match.opp_tag = matchInfo['UserOpp']['tagline']
                match.opp_sumLevel = matchInfo['UserOpp']['sumLvl']
                match.opp_role = matchInfo['UserOpp']['role']
                match.save(update_fields=['opp_username', 'opp_tag', 'opp_sumLevel','opp_role'])
                self.request.session['match_code'] = match.code
                 # .data returns the json formatted data from the room object in question coming
                # from the request
                # ALSO returns response for a stable, updated room for an existing session
                return Response(MatchSerializer(match).data, status.HTTP_200_OK)
            else:
                match = Match(
                    host = host,
                    username = username,
                    tag = tag
                )
                match.save()
                #Beginning of generating stats------------------------------
                matchInfo = generateInfo(username, tag)
                #user Model Fields
                match.user_sumLevel = matchInfo['User']['sumLvl']
                match.user_role = matchInfo['User']['role']
                match.save(update_fields=['user_sumLevel', 'user_role'])
                #Opp Model Fields
                match.opp_username = matchInfo['UserOpp']['username']
                match.opp_tag = matchInfo['UserOpp']['tagline']
                match.opp_sumLevel = matchInfo['UserOpp']['sumLvl']
                match.opp_role = matchInfo['UserOpp']['role']
                match.save(update_fields=['opp_username', 'opp_tag', 'opp_sumLevel','opp_role'])
                self.request.session['match_code'] = match.code
                return Response(MatchSerializer(match).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)