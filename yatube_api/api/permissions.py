from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied, NotAuthenticated


class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated or request.method == 'GET':
            return True
        raise NotAuthenticated

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user or request.method == 'GET':
            return True
        raise PermissionDenied('Изменение чужого контента запрещено!')
