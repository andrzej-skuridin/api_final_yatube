from rest_framework import (filters,
                            status,
                            viewsets)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from api.permissions import AuthorOrReadOnly, AuthGetOrPostOnly
from api.serializers import (CommentSerializer,
                             FollowSerializer,
                             GroupSerializer,
                             PostSerializer)
from posts.models import (Comment,
                          Follow,
                          Group,
                          Post)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [AuthorOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post=post_id)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]  # не годится, он разрешает PUT и PATCH, зато работает
    #permission_classes = [AuthGetOrPostOnly] # работает некорректно
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        if self.kwargs.get('following') == self.request.user:
            # нельзя подписаться на себя
            return status.HTTP_400_BAD_REQUEST
        # это тоже не работает
        if serializer.data is None:
            return status.HTTP_400_BAD_REQUEST
        if self.kwargs.get('following') is None:
            return status.HTTP_400_BAD_REQUEST
        if self.kwargs.get('following') == {}:
            return status.HTTP_400_BAD_REQUEST
