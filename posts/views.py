from rest_framework import generics 
from .serializers import PostSerializer
from .models import Post


class PostsListApi(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class= PostSerializer



class PostDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class= PostSerializer    