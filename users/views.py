from typing import Any
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets

from .use_cases.signup import SignupUseCase
from .use_cases.signup_api import SignupApiUseCase
from .use_cases.login import LoginUseCase
from .use_cases.login_api import LoginApiUseCase

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for authenticating users.

    Attributes
    ----------
    signup_use_case : SignupUseCase
        The use case for signing up a user.
    login_use_case : LoginUseCase
        The use case for logging in a user.
        
    Methods
    -------
    signup(request)
        Sign up a user.
    login(request)
        Log in a user.
    test_token(request)
        Test a token.
    """
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.signup_use_case: SignupUseCase = SignupApiUseCase()
        self.login_use_case: LoginUseCase = LoginApiUseCase()

    @action(
        methods=['post'], 
        detail=False, 
        permission_classes=[AllowAny], 
        url_path='signup', 
        url_name='signup',
    )
    def signup(self, request)-> Response:
        """Sign up a user.
        Parameters
        ----------
        request : Request
            The request object.

        Returns
        -------
        Response
            The response object.
        """
        return self.signup_use_case.signup(request.data)
        
        
    @action(
        methods=['post'], 
        detail=False, 
        permission_classes=[AllowAny], 
        url_path='login', 
        url_name='login',
    )
    def login(self, request)-> Response:
        """Log in a user.
        Parameters
        ----------
        request : Request
            The request object.

        Returns
        -------
        Response
            The response object.
        """
        return self.login_use_case.login(request.data['username'], request.data['password'])
    
    @action(
        methods=['get'], 
        detail=False, 
        permission_classes=[IsAuthenticated],
        authentication_classes=[SessionAuthentication, TokenAuthentication], 
        url_path='test_token', 
        url_name='test_token',
    )
    def test_token(self, request)-> Response:
        """Test a token.
        Parameters
        ----------
        request : Request
            The request object.

        Returns
        -------
        Response
            The response object.
        """
        return Response("passed!")
