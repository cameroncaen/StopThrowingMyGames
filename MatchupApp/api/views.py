from django.shortcuts import render
from rest_framework import generics, status
from .serializers import MatchSerializer, PopulateMatchupInfoSerializer
from .models import Match
from rest_framework.views import APIView
from rest_framework.response import Response

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

class PopulateMatchupInfo(APIView):
    serializer_class = PopulateMatchupInfoSerializer
     
    def getPlayerInfo(username, tag):
        #access API for user instance and return it
        print(username)

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
                self.request.session['match_code'] = match.code
                return Response(MatchSerializer(match).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)