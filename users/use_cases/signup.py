from abc import ABC, abstractmethod
from django.http import HttpResponseBase

class SignupUseCase(ABC):
    """
    SignupUseCase is an abstract class that defines the methods that must be
    implemented by the SignupUseCaseImpl class.
    """
    @abstractmethod
    def signup(self, user_data: dict)-> HttpResponseBase:
        """Sign up a user.
        Parameters
        ----------
        user_data : dict
            The user data to use for signing up.

        Returns
        -------
        HttpResponseBase
            The response object.
        """
        pass