from django.urls import path
from .views import CategoryList, CategoryDetail, TagList, TagDetail, UserStatusList, UserStatusDetail, UserList, UserDetail, ContentList, ContentDetail, RepositoryList, RepositoryDetail, SubscribeList, SubscribeDetail, CommentStatusList, CommentStatusDetail, CommentList, CommentDetail, ContentCategoryMapList, ContentTagMapList, UserTagMapList

urlpatterns = [
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),
    path('tag/', TagList.as_view()),
    path('tag/<int:pk>/', TagDetail.as_view()),
    path('user-status/', UserStatusList.as_view()),
    path('user-status/<int:pk>/', UserStatusDetail.as_view()),
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('content/', ContentList.as_view()),
    path('content/<int:pk>/', ContentDetail.as_view()),
    path('repository/', RepositoryList.as_view()),
    path('repository/<int:pk>/', RepositoryDetail.as_view()),
    path('subscribe/', SubscribeList.as_view()),
    path('subscribe/<int:pk>/', SubscribeDetail.as_view()),
    path('comment-status/', CommentStatusList.as_view()),
    path('comment-status/<int:pk>/', CommentStatusDetail.as_view()),
    path('comment/', CommentList.as_view()),
    path('comment/<int:pk>/', CommentDetail.as_view()),
    path('content-category-map/', ContentCategoryMapList.as_view()),
    path('content-tag-map/', ContentTagMapList.as_view()),
    path('user-tag-map/', UserTagMapList.as_view()),
]
