from django.shortcuts import render
from rest_framework import generics
from .serializers import MatchSerializer
from .models import Match

# Create your views here.
# using .ListApiView is for seeing the views rather than generating them
# REACT ALLOWS FOR THE CODE TO GENERATE THESE RATHER THAN THE UI ON THE BROWSER CURRENTLY
class MatchView(generics.CreateAPIView):
    # What do we want to return?
    queryset = Match.objects.all()
    # How do I convert these Match objects into a readable/usable format?
    serializer_class = MatchSerializer