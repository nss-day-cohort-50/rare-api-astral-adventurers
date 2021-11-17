"""Handle all HTTP requests for posts"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rareapi.models import Post

class PostView(ViewSet):
    """Rare posts"""

    def list(self, request):
        """Handles GET request for all games

        Returns:
            Response -- JSON serialized list of games
        """

        posts = Post.objects.all()

        posts_serial = PostSerializer(posts, many=True, context = {'request': request})
        # No need for a context since we're using ModelSerializer.

        return Response(posts_serial.data)

class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts
    
    Arguments:
        serializer type
    """
    class Meta:
        model = Post
        fields = ('id', 'author', 'category', 'title', 'content', 'image_url', 'publication_date', 'is_published', 'approved')
        depth = 1