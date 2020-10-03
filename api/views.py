from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import BoastRoastSerializer
from ghostPost.models import Boast_Roast

class BoastRoastViewset(viewsets.ModelViewSet):
    queryset = Boast_Roast.objects.all().order_by("-date_created")
    serializer_class = BoastRoastSerializer

    @action(detail=True, methods=['get', 'post'])
    def up_vote(self, request, pk=None):
        vote = self.get_object()
        vote.total_votes += 1
        vote.save()
        return Response(vote.total_votes)

    @action(detail=True, methods=['get', 'post'])
    def down_vote(self, request, pk=None):
        vote = self.get_object()
        vote.total_votes -= 1
        vote.save()
        return Response(vote.total_votes)



