from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Follow, Group, Post


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = ('title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    # этот тип поля работает только на чтение, не годится
    # для создания поста
    following = serializers.StringRelatedField()

    # надо как-то так?
    #following = serializers.SlugRelatedField(
    #    many=True,
    #    slug_field='following',
    #    queryset=Follow.objects.filter(user=)
    #)

    class Meta:
        model = Follow
        fields = ('following', 'user')
