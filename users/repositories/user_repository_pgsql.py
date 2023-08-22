from users.repositories.user_repository import UserRepository
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class UserRepositoryPgsql(UserRepository):
    """
    UserRepositoryPgsql is a class that implements the UserRepository abstract
    class.

    Methods
    -------
    get_by_username(username)
        Get a user by username.
    get_object_or_404(username)
        Get a user by username or return 404.
    """
    def get_by_username(self, username: str)-> User:
        """Get a user by username.
        Parameters
        ----------
        username : str
            The username of the user to get.
        
        Returns
        -------
        User
            The user retrieved.
        """
        return User.objects.get(username=username)
    def get_object_or_404(self, username: str)-> User:
        """Get a user by username or return 404.
        Parameters
        ----------
        username : str
            The username of the user to get.

        Returns
        -------
        User
            The user retrieved.
        """
        return get_object_or_404(User, username=username)