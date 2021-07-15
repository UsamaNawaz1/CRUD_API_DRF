from django.contrib import admin
from django.urls import path, include
from .views import DetailPost, PostList
urlpatterns = [
    path('<int:pk>/', DetailPost.as_view()),
    path('', PostList.as_view())

]