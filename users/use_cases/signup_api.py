from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from ..serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .signup import SignupUseCase
from ..repositories.user_repository_pgsql import UserRepositoryPgsql
from ..repositories.user_repository import UserRepository
from ..repositories.token_repository_pgsql import TokenRepositoryPgsql
from ..repositories.token_repository import TokenRepository

class SignupApiUseCase(SignupUseCase):
    """
    SignupApiUseCase is a class that implements the SignupUseCase abstract class.
    
    Attributes
    ----------
    user_repository : UserRepository
        The user repository.
    token_repository : TokenRepository
        The token repository.
        
    Methods
    -------
    signup(user_data)
        Sign up a user.
    """
    def __init__(self) -> None:
        super().__init__()
        self.user_repository : UserRepository = UserRepositoryPgsql()
        self.token_repository : TokenRepository = TokenRepositoryPgsql()

    def signup(self, user_data: dict)-> Response:
        """Sign up a user.
        Parameters
        ----------
        user_data : dict
            The user data to use for signing up.

        Returns
        -------
        Response
            The response of the signup.
        """
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            user = self.user_repository.get_by_username(user_data['username'])
            user.set_password(user_data['password'])
            user.save()
            token = self.token_repository.create(user)
            return Response({'token': token.key, 'user': serializer.data})
        return Response(serializer.errors, status=status.HTTP_200_OK)
