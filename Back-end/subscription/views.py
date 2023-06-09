from .serializers import *
from rest_framework.generics import *

# Create your views here.

class CategoryList(ListAPIView, CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagList(ListAPIView, CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class UserStatusList(ListAPIView, CreateAPIView):
    queryset = UserStatus.objects.all()
    serializer_class = UserStatusSerializer


class UserStatusDetail(RetrieveUpdateDestroyAPIView):
    queryset = UserStatus.objects.all()
    serializer_class = UserStatusSerializer


class UserList(ListAPIView, CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContentList(ListAPIView, CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ContentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class RepositoryList(ListAPIView, CreateAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer


class RepositoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer


class SubscribeList(ListAPIView, CreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer


class SubscribeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer


class CommentStatusList(ListAPIView, CreateAPIView):
    queryset = CommentStatus.objects.all()
    serializer_class = CommentStatusSerializer


class CommentStatusDetail(RetrieveUpdateDestroyAPIView):
    queryset = CommentStatus.objects.all()
    serializer_class = CommentStatusSerializer


class CommentList(ListAPIView, CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ContentCategoryMapList(ListAPIView, CreateAPIView):
    queryset = ContentCategoryMap.objects.all()
    serializer_class = ContentCategoryMapSerializer


class ContentTagMapList(ListAPIView, CreateAPIView):
    queryset = ContentTagMap.objects.all()
    serializer_class = ContentTagMapSerializer


class UserTagMapList(ListAPIView, CreateAPIView):
    queryset = UserTagMap.objects.all()
    serializer_class = UserTagMapSerializer
