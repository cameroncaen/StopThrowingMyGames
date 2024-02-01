from django.shortcuts import render
from rest_framework import generics, status
from .serializers import MatchSerializer, PopulateMatchupInfoSerializer
from .riot_api import GetUserInfo, GetInfoFromLiveMatch, lookupAccount, lookupSummoner
from .get_stats import pullMatchData
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
def findRoles(players):
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



def checkValidity(username, tag):
    try:
        userData = GetUserInfo(username, tag)
        
    except:
        return {'Bad Request': 'Invalid Playername or RiotTag'}
    try:
        players = GetInfoFromLiveMatch(str(userData["id"]))
    except:
        return {'Bad Request': 'This user is not currently in a game'}
    return {'userData': userData, 'players': players}


def generateInfo(userData, players):
    #-------Match Fetched at this point and returned as list of player dictionaries----------
    # Define Puuid variables to store user info 
    allRoles = ['TOP', 'JUNGLE', 'MIDDLE', 'BOTTOM',  'UTILITY']
    userPuuid = userData['puuid']
    userOppPuuid = ''
    allyPuuid = ''
    oppPuuid= ''
    roles = findRoles(players)
    #print(roles)
    ally = ''
    enemy = ''
    if (userPuuid) in (roles['team1']):
        ally = 'team1'
        enemy = 'team2'
    else :
        ally = 'team2'
        enemy = 'team1'
    userRole = roles[ally][userPuuid]['role']

    #------Roles are determined with the git import and User's team is declared from list of players----
    #------team1 refers to players[0-4] and team2 refers to players[5-9]--------------------------------
    
    
    for key in roles[enemy]:
        if roles[enemy][key]['role'] == userRole:
            userOppPuuid = key
            break
    #oppNum = roles[enemy][oppPuuid]['number']
    #-----------Lookup User Opponent to populate stats -------------------------------------------------
    OppAcct = lookupAccount(userOppPuuid)
    OppSumm = lookupSummoner(userOppPuuid)
    #------Nested Dictionaries under lebel allMatchData are declared to be updated below ---------------
    # Note, alt lanes are organized to be in the order TOP ->  JG -> MID -> ADC -> SUP. excluding the user's role
    allMatchData = {
        "User": {
            "sumLvl": userData['summonerLevel'],
            "role" : userRole
        },
        "UserOpp": {
            'username': OppAcct['gameName'],
            'tagline': OppAcct['tagLine'],
            "sumLvl": OppSumm['summonerLevel'],
            "role" : roles[enemy][userOppPuuid]['role']
        },
        "AltLane1": {

        },
        "AltLaneOpp1": {

        },
        "AltLane1Blurbs": {

        },
        "AltLane2": {

        },
        "AltLaneOpp2": {

        },
        "AltLane2Blurbs": {

        },
        "AltLane3": {

        },
        "AltLaneOpp3": {

        },
        "AltLane3Blurbs": {

        },
        "AltLane4": {

        },
        "AltLaneOpp4": {

        },
        "AltLane4Blurbs": {

        }
    }
    
    count = 1
    for lane in allRoles:
        if lane == userRole:
            print('HERE')
            #allMatchData['User']['stats'] = pullMatchData(userPuuid, lane)
            #allMatchData['UserOpp']['stats'] = pullMatchData(userOppPuuid, lane)
        else:
            for key in roles[ally]:
                if roles[ally][key]['role'] == lane:
                    allyPuuid = key
                    allMatchData['AltLane'+str(count)]= pullMatchData(allyPuuid, lane)
                    break
            for key in roles[enemy]:
                if roles[enemy][key]['role'] == lane:
                    oppPuuid = key
                    allMatchData['AltLaneOpp'+str(count)] = pullMatchData(oppPuuid, lane)
                    break
            count += 1


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
                validCheck = checkValidity(username, tag)
                if 'Bad Request' in validCheck:
                    return Response({'error': validCheck['Bad Request']}, status=status.HTTP_404_NOT_FOUND)
                else:
                    matchInfo = generateInfo(validCheck['userData'], validCheck['players'])
                # TRY TO HAVE SAVE USE __ALL__ TO ACCOMPLISH UPDATING THE MODEL IN A SINGLE LINE
                #user Model Fields ---------------------------
                match.user_sumLevel = matchInfo['User']['sumLvl']
                match.user_role = matchInfo['User']['role']
                match.save(update_fields=['user_sumLevel', 'user_role'])
                #Opp Model Fields
                match.opp_username = matchInfo['UserOpp']['username']
                match.opp_tag = matchInfo['UserOpp']['tagline']
                match.opp_sumLevel = matchInfo['UserOpp']['sumLvl']
                match.opp_role = matchInfo['UserOpp']['role']
                match.save(update_fields=['opp_username', 'opp_tag', 'opp_sumLevel','opp_role'])
                #Ally1 Model Fields -----------------------------
                match.ally1_username = matchInfo['AltLane1']['username']
                match.ally1_tag = matchInfo['AltLane1'] ['role']
                match.ally1_sumLevel = matchInfo['AltLane1']['sumLvl']
                match.ally1_role = matchInfo['AltLane1']['role']
                match.save(update_fields=['ally1_username', 'ally1_tag', 'ally1_sumLevel','ally1_role'])
                #Enemy1 Model Fields
                match.enemy1_username = matchInfo['AltLaneOpp1']['username']
                match.enemy1_tag = matchInfo['AltLaneOpp1']['tagline']
                match.enemy1_sumLevel = matchInfo['AltLaneOpp1']['sumLvl']
                match.enemy1_role = matchInfo['AltLaneOpp1']['role']
                match.save(update_fields=['enemy1_username', 'enemy1_tag', 'enemy1_sumLevel','enemy1_role'])
                #Ally2 Model Fields -----------------------------
                match.ally2_username = matchInfo['AltLane2']['username']
                match.ally2_tag = matchInfo['AltLane2'] ['role']
                match.ally2_sumLevel = matchInfo['AltLane2']['sumLvl']
                match.ally2_role = matchInfo['AltLane2']['role']
                match.save(update_fields=['ally2_username', 'ally2_tag', 'ally2_sumLevel','ally2_role'])
                #Enemy2 Model Fields
                match.enemy2_username = matchInfo['AltLaneOpp2']['username']
                match.enemy2_tag = matchInfo['AltLaneOpp2']['tagline']
                match.enemy2_sumLevel = matchInfo['AltLaneOpp2']['sumLvl']
                match.enemy2_role = matchInfo['AltLaneOpp2']['role']
                match.save(update_fields=['enemy2_username', 'enemy2_tag', 'enemy2_sumLevel','enemy2_role'])
                #Ally3 Model Fields -----------------------------
                match.ally3_username = matchInfo['AltLane3']['username']
                match.ally3_tag = matchInfo['AltLane3'] ['role']
                match.ally3_sumLevel = matchInfo['AltLane3']['sumLvl']
                match.ally3_role = matchInfo['AltLane3']['role']
                match.save(update_fields=['ally3_username', 'ally3_tag', 'ally3_sumLevel','ally3_role'])
                #Enemy3 Model Fields
                match.enemy3_username = matchInfo['AltLaneOpp3']['username']
                match.enemy3_tag = matchInfo['AltLaneOpp3']['tagline']
                match.enemy3_sumLevel = matchInfo['AltLaneOpp3']['sumLvl']
                match.enemy3_role = matchInfo['AltLaneOpp3']['role']
                match.save(update_fields=['enemy3_username', 'enemy3_tag', 'enemy3_sumLevel','enemy3_role'])
                #Ally4 Model Fields -----------------------------
                match.ally4_username = matchInfo['AltLane4']['username']
                match.ally4_tag = matchInfo['AltLane4'] ['role']
                match.ally4_sumLevel = matchInfo['AltLane4']['sumLvl']
                match.ally4_role = matchInfo['AltLane4']['role']
                match.save(update_fields=['ally4_username', 'ally4_tag', 'ally4_sumLevel','ally4_role'])
                #Enemy4 Model Fields
                match.enemy4_username = matchInfo['AltLaneOpp4']['username']
                match.enemy4_tag = matchInfo['AltLaneOpp4']['tagline']
                match.enemy4_sumLevel = matchInfo['AltLaneOpp4']['sumLvl']
                match.enemy4_role = matchInfo['AltLaneOpp4']['role']
                match.save(update_fields=['enemy4_username', 'enemy4_tag', 'enemy4_sumLevel','enemy4_role'])



                
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
                validCheck = checkValidity(username, tag)
                if 'Bad Request' in validCheck:
                    return Response({'error': validCheck['Bad Request']}, status=status.HTTP_404_NOT_FOUND)
                else:
                    matchInfo = generateInfo(validCheck['userData'], validCheck['players'])
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
