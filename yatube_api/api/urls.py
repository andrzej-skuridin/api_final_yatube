from django.urls import include, path
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken import views
from api.views import (PostViewSet, GroupViewSet, CommentViewSet)



router = routers.SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
