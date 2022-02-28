from rest_framework.viewsets import ModelViewSet
from .models import *
from rest_framework.generics import *
from .serializers import *

class MediaCreate(CreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class MediaDelete(DestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class LikeCreateList(ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeDelete(DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer




