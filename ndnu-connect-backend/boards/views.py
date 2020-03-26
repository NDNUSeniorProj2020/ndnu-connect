from rest_framework import viewsets

from importlib import import_module

from .models import Board, Topic, Post
from .serializers import BoardSerializer, TopicSerializer, PostSerializer


acc = import_module('accounts.models')


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
