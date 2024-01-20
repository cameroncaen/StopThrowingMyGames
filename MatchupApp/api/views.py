from django.shortcuts import render
from rest_framework import generics
from .serializers import MatchSerializer, PopulateMatchupInfoSerializer
from .models import Match
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# using .ListApiView is for seeing the views rather than generating them
# REACT ALLOWS FOR THE CODE TO GENERATE THESE RATHER THAN THE UI ON THE BROWSER CURRENTLY
class MatchView(generics.CreateAPIView):
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