from rest_framework import serializers
from .models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('__all__')

# Incoiming Serializer: i.e. processes data/requests coming from webpage
class PopulateMatchupInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('username', 'tag')