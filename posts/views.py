from rest_framework import generics , permissions
from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthororReadOnly


class PostsListApi(generics.ListCreateAPIView):
    permission_classes = (IsAuthororReadOnly,)
    queryset = Post.objects.all()
    serializer_class= PostSerializer



class PostDetailApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthororReadOnly,)
    queryset = Post.objects.all()
    serializer_class= PostSerializer    