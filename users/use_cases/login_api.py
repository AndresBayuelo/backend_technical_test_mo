from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from ..serializers import UserSerializer
from .login import LoginUseCase
from ..repositories.user_repository_pgsql import UserRepositoryPgsql
from ..repositories.user_repository import UserRepository
from ..repositories.token_repository_pgsql import TokenRepositoryPgsql
from ..repositories.token_repository import TokenRepository

class LoginApiUseCase(LoginUseCase):
    """
    LoginApiUseCase is a class that implements the LoginUseCase abstract class.
    
    Attributes
    ----------
    user_repository : UserRepository
        The user repository.
    token_repository : TokenRepository
        The token repository.
    
    Methods
    -------
    login(username, password)
        Log in a user.
    """
    def __init__(self) -> None:
        super().__init__()
        self.user_repository : UserRepository = UserRepositoryPgsql()
        self.token_repository : TokenRepository = TokenRepositoryPgsql()

    def login(self, username: str, password: str)-> Response:
        """Log in a user.
        Parameters
        ----------
        username : str
            The username of the user to log in.
        password : str
            The password of the user to log in.

        Returns
        -------
        Response
            The response of the login.
        """
        user = self.user_repository.get_object_or_404(username)
        if not user.check_password(password):
            return Response("missing user", status=status.HTTP_404_NOT_FOUND)
        token, created = self.token_repository.get_or_create(user)
        serializer = UserSerializer(user)
        return Response({'token': token.key, 'user': serializer.data})