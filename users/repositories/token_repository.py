from abc import ABC, abstractmethod
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class TokenRepository(ABC):
    """
    TokenRepository is an abstract class that defines the methods that must be 
    implemented by the TokenRepositoryPgsql class.

    Methods
    -------
    create(user)
        Create a token for a user.
    get_or_create(user)
        Get or create a token for a user.
    """
    @abstractmethod
    def create(self, user: User) -> Token:
        """Create a token for a user.
        Parameters
        ----------
        user : User
            The user to create a token for.

        Returns
        -------
        Token
            The token created.
        """
        pass
    @abstractmethod
    def get_or_create(self, user: User) -> Token:
        """Get or create a token for a user.
        Parameters
        ----------
        user : User
            The user to get or create a token for.

        Returns
        -------
        Token
            The token created or retrieved.
        """
        pass