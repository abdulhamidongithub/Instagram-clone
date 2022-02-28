from .models import Like,Message,Media,Comment,Comment_like,Post,Saved
from rest_framework.serializers import ModelSerializer

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class SavedSerializer(ModelSerializer):
    class Meta:
        model = Saved
        fields = '__all__'

class Comment_likeSerializer(ModelSerializer):
    class Meta:
        model = Comment_like
        fields = '__all__'

