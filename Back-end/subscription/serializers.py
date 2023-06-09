from rest_framework.serializers import ModelSerializer
from .models import *


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UserStatusSerializer(ModelSerializer):
    class Meta:
        model = UserStatus
        fields = '__all__'


class UserSerializer(ModelSerializer):
    tag = TagSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'

        
class ContentSerializer(ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = '__all__'


class RepositorySerializer(ModelSerializer):
    class Meta:
        model = Repository
        fields = '__all__'


class SubscribeSerializer(ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'


class CommentStatusSerializer(ModelSerializer):
    class Meta:
        model = CommentStatus
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ContentCategoryMapSerializer(ModelSerializer):
    class Meta:
        model = ContentCategoryMap
        fields = '__all__'


class ContentTagMapSerializer(ModelSerializer):
    class Meta:
        model = ContentTagMap
        fields = '__all__'


class UserTagMapSerializer(ModelSerializer):
    class Meta:
        model = UserTagMap
        fields = '__all__'