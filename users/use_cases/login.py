from abc import ABC, abstractmethod
from django.http import HttpResponseBase

class LoginUseCase(ABC):
    """
    LoginUseCase is an abstract class that defines the methods that must be
    implemented by the LoginUseCaseImpl class.
    """
    @abstractmethod
    def login(self, username: str, password: str)-> HttpResponseBase:
        """Log in a user.
        Parameters
        ----------
        username : str
            The username of the user to log in.
        password : str
            The password of the user to log in.

        Returns
        -------
        HttpResponseBase
            The response object.
        """
        pass