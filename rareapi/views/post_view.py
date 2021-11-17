"""Handle all HTTP requests for posts"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post
from rest_framework.decorators import action


class PostView(ViewSet):
    """Rare posts"""

    def list(self, request):
        """Handles GET request for all games

        Returns:
            Response -- JSON serialized list of games
        """

        posts = Post.objects.all()

        # Support filtering games by author
        #   http://localhost:8000/posts?author_id=${authorId}
        #
        # That URL will retrieve all posts by specific user
        author = self.request.query_params.get('author', None)
        if author is not None:
            posts = posts.filter(author__id=author)

        posts_serial = PostSerializer(
            posts, many=True, context={'request': request})
        # No need for a context since we're using ModelSerializer.

        return Response(posts_serial.data)

    @action(methods=['put'], detail=True)
    def publish(self, request, pk=None):
        """Managing publish / unpublish buttons"""

        post = Post.objects.get(pk=pk)

        if post.is_published is not True:
            post.is_published = True
            post.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        else:
            post.is_published = False
            post.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)

class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts

    Arguments:
        serializer type
    """
    class Meta:
        model = Post
        fields = ('id', 'author', 'category', 'title', 'content',
                  'image_url', 'publication_date', 'is_published', 'approved')
        depth = 1
