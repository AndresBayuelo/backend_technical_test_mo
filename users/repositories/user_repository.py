from abc import ABC, abstractmethod
from django.contrib.auth.models import User

class UserRepository(ABC):
    """
    UserRepository is an abstract class that defines the methods that must be
    implemented by the UserRepositoryPgsql class.

    Methods
    -------
    get_by_username(username)
        Get a user by username.
    get_object_or_404(username)
        Get a user by username or return 404.
    """
    @abstractmethod
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
        pass
    @abstractmethod
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
        pass