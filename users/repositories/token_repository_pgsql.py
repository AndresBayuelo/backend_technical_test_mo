from users.repositories.token_repository import TokenRepository
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class TokenRepositoryPgsql(TokenRepository):
    """
    TokenRepositoryPgsql is a class that implements the TokenRepository abstract
    class.
    
    Methods
    -------
    create(user)
        Create a token for a user.
    get_or_create(user)
        Get or create a token for a user.
    """
    def create(self, user: User)-> Token:
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
        return Token.objects.create(user=user)
    def get_or_create(self, user: User)-> Token:
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
        return Token.objects.get_or_create(user=user)