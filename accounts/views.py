from django.shortcuts import render

from rest_framework import generics

from .models import post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer
