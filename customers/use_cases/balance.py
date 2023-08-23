from abc import ABC, abstractmethod

from django.http import HttpResponseBase


class BalanceUseCase(ABC):
    """
    BalanceUseCase is an abstract class that defines the BalanceUseCase interface.

    Attributes
    ----------
    None

    Methods
    -------
    get(external_id)
        Get the balance of a customer.
    """
    @abstractmethod
    def get(self, external_id: str)-> HttpResponseBase:
        """Get the balance of a customer.

        Parameters
        ----------
        external_id : str
            The external id of the customer to get the balance.

        Returns
        -------
        HttpResponseBase
            The response of the request.
        """
        pass