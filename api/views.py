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

    @action(detail=False)
    def total(self, request):
        posts = Boast_Roast.objects.all().order_by('-total_votes')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roasts(self, request):
        roast_posts = Boast_Roast.objects.filter(post_type=False)
        serializer = self.get_serializer(roast_posts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def boasts(self, request):
        boast_posts = Boast_Roast.objects.filter(post_type=True)
        serializer = self.get_serializer(boast_posts, many=True)
        return Response(serializer.data)

    # @action(detail=False)
    # def up_vote(self, request):
    #     boast_posts = Boast_Roast.objects.filter(post_type=True)
    #     serializer = self.get_serializer(boast_posts, many=True)
    #     return Response(serializer.data)

    # @action(detail=False)
    # def down_vote(self, request):
    #     boast_posts = Boast_Roast.objects.filter(post_type=True)
    #     serializer = self.get_serializer(boast_posts, many=True)
    #     return Response(serializer.data)