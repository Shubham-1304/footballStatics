from .serializers import OverallScore
from players.models import Player
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg


class PlayersAbove90(APIView):
    def get(self,request,format=None):
        players=Player.objects.filter(overall__gt=90).order_by('-overall')
        serializer=OverallScore(players,many=True)
        return Response(serializer.data)


class OverallNational(APIView):
    def get(self,request,format=None):
        player = (Player.objects.values('nationality')).annotate(averageOfOverall=Avg('overall')).order_by()
        return Response(player)
