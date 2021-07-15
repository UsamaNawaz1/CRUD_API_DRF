from django.shortcuts import render

from rest_framework import generics, permissions

from .models import post
from .serializers import PostSerializer
from .permissions import AuthorOrReadOnly

class PostList(generics.ListCreateAPIView):
    
    def get_queryset(self):
        posts = post.objects.filter(author=self.request.user)
        return posts
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AuthorOrReadOnly,)
    queryset = post.objects.all()
    serializer_class = PostSerializer
