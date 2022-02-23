from rest_framework import serializers
from players.models import Player

class OverallScore(serializers.ModelSerializer):
    class Meta:
        model=Player
        fields=['name','overall']