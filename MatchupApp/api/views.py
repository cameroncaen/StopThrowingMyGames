from django.shortcuts import render
from rest_framework import generics, status
from .serializers import MatchSerializer, PopulateMatchupInfoSerializer
from .riot_api import GetUserInfo, GetInfoFromLiveMatch, lookupAccount, lookupSummoner
from .get_stats import pullMatchData
from .blurbs import genBlurbs
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

    #oppNum = roles[enemy][oppPuuid]['number']
    #-----------Lookup User Opponent to populate stats -------------------------------------------------

    #------Nested Dictionaries under lebel allMatchData are declared to be updated below ---------------
    # Note, alt lanes are organized to be in the order TOP ->  JG -> MID -> ADC -> SUP. excluding the user's role
    allMatchData = {
        "User": {
            "sumLvl": userData['summonerLevel'],
            "role" : userRole
        },
        "UserOpp": {

        },
        "UserLaneBlurbs": {

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
            for key in roles[enemy]:
                if roles[enemy][key]['role'] == lane:
                    userOppPuuid = key
                    break
            allMatchData['User']['stats'] = pullMatchData(userPuuid, lane, roles[ally][userPuuid]['champId'], 2)
            allMatchData['UserOpp'] = pullMatchData(userOppPuuid, lane, roles[enemy][userOppPuuid]['champId'], 1)
            allMatchData['UserLaneBlurbs'] = genBlurbs(allMatchData['User']['stats'], allMatchData['UserOpp']['stats'], lane)
        else:
            for key in roles[ally]:
                if roles[ally][key]['role'] == lane:
                    allyPuuid = key
                    allMatchData['AltLane'+str(count)]= pullMatchData(allyPuuid, lane, roles[ally][key]['champId'], 0)
                    break
            for key in roles[enemy]:
                if roles[enemy][key]['role'] == lane:
                    oppPuuid = key
                    allMatchData['AltLaneOpp'+str(count)] = pullMatchData(oppPuuid, lane, roles[enemy][key]['champId'], 0)
                    break
            allMatchData['AltLane'+str(count)+'Blurbs'] = genBlurbs(allMatchData['AltLane'+str(count)]['stats'], allMatchData['AltLaneOpp'+str(count)]['stats'], lane)
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
                match.user_kills = matchInfo['User']['stats']['kills']
                match.user_deaths = matchInfo['User']['stats']['deaths']
                match.user_assists = matchInfo['User']['stats']['assists']
                match.user_wardsPlaced = matchInfo['User']['stats']['wardsPlaced']
                match.user_wardsKilled = matchInfo['User']['stats']['wardsKilled']
                match.user_VWBought = matchInfo['User']['stats']['visionWardsBoughtInGame']
                match.user_KP = matchInfo['User']['stats']['KP']
                match.user_GPM = matchInfo['User']['stats']['GPM']
                match.user_DPM =matchInfo['User']['stats']['DPM']
                match.save(update_fields=['user_sumLevel', 'user_role', 'user_kills', 'user_deaths', 'user_assists',
                                          'user_wardsPlaced', 'user_wardsKilled', 'user_VWBought', 'user_KP', 'user_GPM', 'user_DPM'])
                #Opp Model Fields
                match.opp_username = matchInfo['UserOpp']['username']
                match.opp_tag = matchInfo['UserOpp']['tagline']
                match.opp_sumLevel = matchInfo['UserOpp']['sumLvl']
                match.opp_role = matchInfo['UserOpp']['role']
                match.opp_kills = matchInfo['UserOpp']['stats']['kills']
                match.opp_deaths = matchInfo['UserOpp']['stats']['deaths']
                match.opp_assists = matchInfo['UserOpp']['stats']['assists']
                match.opp_wardsPlaced = matchInfo['UserOpp']['stats']['wardsPlaced']
                match.opp_wardsKilled = matchInfo['UserOpp']['stats']['wardsKilled']
                match.opp_VWBought = matchInfo['UserOpp']['stats']['visionWardsBoughtInGame']
                match.opp_KP = matchInfo['UserOpp']['stats']['KP']
                match.opp_GPM = matchInfo['UserOpp']['stats']['GPM']
                match.opp_DPM =matchInfo['UserOpp']['stats']['DPM']
                match.save(update_fields=['opp_username', 'opp_tag', 'opp_sumLevel','opp_role', 'opp_kills', 'opp_deaths', 'opp_assists',
                                          'opp_wardsPlaced', 'opp_wardsKilled', 'opp_VWBought', 'opp_KP', 'opp_GPM', 'opp_DPM'])
                #Ally1 Model Fields -----------------------------
                match.ally1_username = matchInfo['AltLane1']['username']
                match.ally1_tag = matchInfo['AltLane1'] ['tagline']
                match.ally1_sumLevel = matchInfo['AltLane1']['sumLvl']
                match.ally1_role = matchInfo['AltLane1']['role']
                match.ally1_kills = matchInfo['AltLane1']['stats']['kills']
                match.ally1_deaths = matchInfo['AltLane1']['stats']['deaths']
                match.ally1_assists = matchInfo['AltLane1']['stats']['assists']
                match.ally1_wardsPlaced = matchInfo['AltLane1']['stats']['wardsPlaced']
                match.ally1_wardsKilled = matchInfo['AltLane1']['stats']['wardsKilled']
                match.ally1_VWBought = matchInfo['AltLane1']['stats']['visionWardsBoughtInGame']
                match.ally1_KP = matchInfo['AltLane1']['stats']['KP']
                match.ally1_GPM = matchInfo['AltLane1']['stats']['GPM']
                match.ally1_DPM =matchInfo['AltLane1']['stats']['DPM']
                match.save(update_fields=['ally1_username', 'ally1_tag', 'ally1_sumLevel','ally1_role', 'ally1_kills', 'ally1_deaths', 'ally1_assists',
                                          'ally1_wardsPlaced', 'ally1_wardsKilled', 'ally1_VWBought', 'ally1_KP', 'ally1_GPM', 'ally1_DPM'])
                #Enemy1 Model Fields
                match.enemy1_username = matchInfo['AltLaneOpp1']['username']
                match.enemy1_tag = matchInfo['AltLaneOpp1']['tagline']
                match.enemy1_sumLevel = matchInfo['AltLaneOpp1']['sumLvl']
                match.enemy1_role = matchInfo['AltLaneOpp1']['role']
                match.enemy1_kills = matchInfo['AltLaneOpp1']['stats']['kills']
                match.enemy1_deaths = matchInfo['AltLaneOpp1']['stats']['deaths']
                match.enemy1_assists = matchInfo['AltLaneOpp1']['stats']['assists']
                match.enemy1_wardsPlaced = matchInfo['AltLaneOpp1']['stats']['wardsPlaced']
                match.enemy1_wardsKilled = matchInfo['AltLaneOpp1']['stats']['wardsKilled']
                match.enemy1_VWBought = matchInfo['AltLaneOpp1']['stats']['visionWardsBoughtInGame']
                match.enemy1_KP = matchInfo['AltLaneOpp1']['stats']['KP']
                match.enemy1_GPM = matchInfo['AltLaneOpp1']['stats']['GPM']
                match.enemy1_DPM =matchInfo['AltLaneOpp1']['stats']['DPM']
                match.save(update_fields=['enemy1_username', 'enemy1_tag', 'enemy1_sumLevel','enemy1_role', 'enemy1_kills', 'enemy1_deaths', 'enemy1_assists',
                                          'enemy1_wardsPlaced', 'enemy1_wardsKilled', 'enemy1_VWBought', 'enemy1_KP', 'enemy1_GPM', 'enemy1_DPM'])
                #Ally2 Model Fields -----------------------------
                match.ally2_username = matchInfo['AltLane2']['username']
                match.ally2_tag = matchInfo['AltLane2'] ['tagline']
                match.ally2_sumLevel = matchInfo['AltLane2']['sumLvl']
                match.ally2_role = matchInfo['AltLane2']['role']
                match.ally2_kills = matchInfo['AltLane2']['stats']['kills']
                match.ally2_deaths = matchInfo['AltLane2']['stats']['deaths']
                match.ally2_assists = matchInfo['AltLane2']['stats']['assists']
                match.ally2_wardsPlaced = matchInfo['AltLane2']['stats']['wardsPlaced']
                match.ally2_wardsKilled = matchInfo['AltLane2']['stats']['wardsKilled']
                match.ally2_VWBought = matchInfo['AltLane2']['stats']['visionWardsBoughtInGame']
                match.ally2_KP = matchInfo['AltLane2']['stats']['KP']
                match.ally2_GPM = matchInfo['AltLane2']['stats']['GPM']
                match.ally2_DPM =matchInfo['AltLane2']['stats']['DPM']
                match.save(update_fields=['ally2_username', 'ally2_tag', 'ally2_sumLevel','ally2_role', 'ally2_kills', 'ally2_deaths', 'ally2_assists',
                                          'ally2_wardsPlaced', 'ally2_wardsKilled', 'ally2_VWBought', 'ally2_KP', 'ally2_GPM', 'ally2_DPM'])
                #Enemy2 Model Fields
                match.enemy2_username = matchInfo['AltLaneOpp2']['username']
                match.enemy2_tag = matchInfo['AltLaneOpp2']['tagline']
                match.enemy2_sumLevel = matchInfo['AltLaneOpp2']['sumLvl']
                match.enemy2_role = matchInfo['AltLaneOpp2']['role']
                match.enemy2_kills = matchInfo['AltLaneOpp2']['stats']['kills']
                match.enemy2_deaths = matchInfo['AltLaneOpp2']['stats']['deaths']
                match.enemy2_assists = matchInfo['AltLaneOpp2']['stats']['assists']
                match.enemy2_wardsPlaced = matchInfo['AltLaneOpp2']['stats']['wardsPlaced']
                match.enemy2_wardsKilled = matchInfo['AltLaneOpp2']['stats']['wardsKilled']
                match.enemy2_VWBought = matchInfo['AltLaneOpp2']['stats']['visionWardsBoughtInGame']
                match.enemy2_KP = matchInfo['AltLaneOpp2']['stats']['KP']
                match.enemy2_GPM = matchInfo['AltLaneOpp2']['stats']['GPM']
                match.enemy2_DPM =matchInfo['AltLaneOpp2']['stats']['DPM']
                match.save(update_fields=['enemy2_username', 'enemy2_tag', 'enemy2_sumLevel','enemy2_role', 'enemy2_kills', 'enemy2_deaths', 'enemy2_assists',
                                          'enemy2_wardsPlaced', 'enemy2_wardsKilled', 'enemy2_VWBought', 'enemy2_KP', 'enemy2_GPM', 'enemy2_DPM'])
                #Ally3 Model Fields -----------------------------
                match.ally3_username = matchInfo['AltLane3']['username']
                match.ally3_tag = matchInfo['AltLane3'] ['tagline']
                match.ally3_sumLevel = matchInfo['AltLane3']['sumLvl']
                match.ally3_role = matchInfo['AltLane3']['role']
                match.ally3_kills = matchInfo['AltLane3']['stats']['kills']
                match.ally3_deaths = matchInfo['AltLane3']['stats']['deaths']
                match.ally3_assists = matchInfo['AltLane3']['stats']['assists']
                match.ally3_wardsPlaced = matchInfo['AltLane3']['stats']['wardsPlaced']
                match.ally3_wardsKilled = matchInfo['AltLane3']['stats']['wardsKilled']
                match.ally3_VWBought = matchInfo['AltLane3']['stats']['visionWardsBoughtInGame']
                match.ally3_KP = matchInfo['AltLane3']['stats']['KP']
                match.ally3_GPM = matchInfo['AltLane3']['stats']['GPM']
                match.ally3_DPM =matchInfo['AltLane3']['stats']['DPM']
                match.save(update_fields=['ally3_username', 'ally3_tag', 'ally3_sumLevel','ally3_role', 'ally3_kills', 'ally3_deaths', 'ally3_assists',
                                          'ally3_wardsPlaced', 'ally3_wardsKilled', 'ally3_VWBought', 'ally3_KP', 'ally3_GPM', 'ally3_DPM'])
                #Enemy3 Model Fields
                match.enemy3_username = matchInfo['AltLaneOpp3']['username']
                match.enemy3_tag = matchInfo['AltLaneOpp3']['tagline']
                match.enemy3_sumLevel = matchInfo['AltLaneOpp3']['sumLvl']
                match.enemy3_role = matchInfo['AltLaneOpp3']['role']
                match.enemy3_kills = matchInfo['AltLaneOpp3']['stats']['kills']
                match.enemy3_deaths = matchInfo['AltLaneOpp3']['stats']['deaths']
                match.enemy3_assists = matchInfo['AltLaneOpp3']['stats']['assists']
                match.enemy3_wardsPlaced = matchInfo['AltLaneOpp3']['stats']['wardsPlaced']
                match.enemy3_wardsKilled = matchInfo['AltLaneOpp3']['stats']['wardsKilled']
                match.enemy3_VWBought = matchInfo['AltLaneOpp3']['stats']['visionWardsBoughtInGame']
                match.enemy3_KP = matchInfo['AltLaneOpp3']['stats']['KP']
                match.enemy3_GPM = matchInfo['AltLaneOpp3']['stats']['GPM']
                match.enemy3_DPM =matchInfo['AltLaneOpp3']['stats']['DPM']
                match.save(update_fields=['enemy3_username', 'enemy3_tag', 'enemy3_sumLevel','enemy3_role', 'enemy3_kills', 'enemy3_deaths', 'enemy3_assists',
                                          'enemy3_wardsPlaced', 'enemy3_wardsKilled', 'enemy3_VWBought', 'enemy3_KP', 'enemy3_GPM', 'enemy3_DPM'])
                #Ally4 Model Fields -----------------------------
                match.ally4_username = matchInfo['AltLane4']['username']
                match.ally4_tag = matchInfo['AltLane4'] ['tagline']
                match.ally4_sumLevel = matchInfo['AltLane4']['sumLvl']
                match.ally4_role = matchInfo['AltLane4']['role']
                match.ally4_kills = matchInfo['AltLane4']['stats']['kills']
                match.ally4_deaths = matchInfo['AltLane4']['stats']['deaths']
                match.ally4_assists = matchInfo['AltLane4']['stats']['assists']
                match.ally4_wardsPlaced = matchInfo['AltLane4']['stats']['wardsPlaced']
                match.ally4_wardsKilled = matchInfo['AltLane4']['stats']['wardsKilled']
                match.ally4_VWBought = matchInfo['AltLane4']['stats']['visionWardsBoughtInGame']
                match.ally4_KP = matchInfo['AltLane4']['stats']['KP']
                match.ally4_GPM = matchInfo['AltLane4']['stats']['GPM']
                match.ally4_DPM =matchInfo['AltLane4']['stats']['DPM']
                match.save(update_fields=['ally4_username', 'ally4_tag', 'ally4_sumLevel','ally4_role', 'ally4_kills', 'ally4_deaths', 'ally4_assists',
                                          'ally4_wardsPlaced', 'ally4_wardsKilled', 'ally4_VWBought', 'ally4_KP', 'ally4_GPM', 'ally4_DPM'])
                #Enemy4 Model Fields
                match.enemy4_username = matchInfo['AltLaneOpp4']['username']
                match.enemy4_tag = matchInfo['AltLaneOpp4']['tagline']
                match.enemy4_sumLevel = matchInfo['AltLaneOpp4']['sumLvl']
                match.enemy4_role = matchInfo['AltLaneOpp4']['role']
                match.enemy4_kills = matchInfo['AltLaneOpp4']['stats']['kills']
                match.enemy4_deaths = matchInfo['AltLaneOpp4']['stats']['deaths']
                match.enemy4_assists = matchInfo['AltLaneOpp4']['stats']['assists']
                match.enemy4_wardsPlaced = matchInfo['AltLaneOpp4']['stats']['wardsPlaced']
                match.enemy4_wardsKilled = matchInfo['AltLaneOpp4']['stats']['wardsKilled']
                match.enemy4_VWBought = matchInfo['AltLaneOpp4']['stats']['visionWardsBoughtInGame']
                match.enemy4_KP = matchInfo['AltLaneOpp4']['stats']['KP']
                match.enemy4_GPM = matchInfo['AltLaneOpp4']['stats']['GPM']
                match.enemy4_DPM =matchInfo['AltLaneOpp4']['stats']['DPM']
                match.save(update_fields=['enemy4_username', 'enemy4_tag', 'enemy4_sumLevel','enemy4_role', 'enemy4_kills', 'enemy4_deaths', 'enemy4_assists',
                                          'enemy4_wardsPlaced', 'enemy4_wardsKilled', 'enemy4_VWBought', 'enemy4_KP', 'enemy4_GPM', 'enemy4_DPM'])

                match.user_blurb1 = matchInfo["UserLaneBlurbs"]['blurb1']
                match.user_blurb2 = matchInfo["UserLaneBlurbs"]['blurb2']
                match.user_blurb3 = matchInfo["UserLaneBlurbs"]['blurb3']
                match.user_blurb4 = matchInfo["UserLaneBlurbs"]['blurb4']
                match.save(update_fields=['user_blurb1', 'user_blurb2', 'user_blurb3', 'user_blurb4'])
                print(match.user_blurb3)
                match.ally1_blurb1 = matchInfo["AltLane1Blurbs"]['blurb1']
                match.ally1_blurb2 = matchInfo["AltLane1Blurbs"]['blurb2']
                match.ally1_blurb3 = matchInfo["AltLane1Blurbs"]['blurb3']
                match.ally1_blurb4 = matchInfo["AltLane1Blurbs"]['blurb4']
                match.save(update_fields=['ally1_blurb1', 'ally1_blurb2', 'ally1_blurb3', 'ally1_blurb4'])

                match.ally2_blurb1 = matchInfo["AltLane2Blurbs"]['blurb1']
                match.ally2_blurb2 = matchInfo["AltLane2Blurbs"]['blurb2']
                match.ally2_blurb3 = matchInfo["AltLane2Blurbs"]['blurb3']
                match.ally2_blurb4 = matchInfo["AltLane2Blurbs"]['blurb4']
                match.save(update_fields=['ally2_blurb1', 'ally2_blurb2', 'ally2_blurb3', 'ally2_blurb4'])
                
                match.ally3_blurb1 = matchInfo["AltLane3Blurbs"]['blurb1']
                match.ally3_blurb2 = matchInfo["AltLane3Blurbs"]['blurb2']
                match.ally3_blurb3 = matchInfo["AltLane3Blurbs"]['blurb3']
                match.ally3_blurb4 = matchInfo["AltLane3Blurbs"]['blurb4']
                match.save(update_fields=['ally3_blurb1', 'ally3_blurb2', 'ally3_blurb3', 'ally3_blurb4'])

                match.ally4_blurb1 = matchInfo["AltLane4Blurbs"]['blurb1']
                match.ally4_blurb2 = matchInfo["AltLane4Blurbs"]['blurb2']
                match.ally4_blurb3 = matchInfo["AltLane4Blurbs"]['blurb3']
                match.ally4_blurb4 = matchInfo["AltLane4Blurbs"]['blurb4']
                match.save(update_fields=['ally4_blurb1', 'ally4_blurb2', 'ally4_blurb3', 'ally4_blurb4'])
                
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
