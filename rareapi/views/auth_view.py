from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rareapi.models import Author
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new author for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        email=request.data['email'],
        username=request.data['username'],
        password=request.data['password'],
    )

    # Now save the extra info in the levelupapi_gamer table
    author = Author.objects.create(
        user=new_user,
        bio=request.data['bio'],
        profile_img_url=request.data['profile_img_url'],
        created_on=request.data['created_on'],
        active=request.data['active']
    )

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=author.user)
    # Return the token to the client
    data = { 'token': token.key }
    return Response(data)