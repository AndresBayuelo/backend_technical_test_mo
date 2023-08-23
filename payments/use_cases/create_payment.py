from abc import ABC, abstractmethod

from django.http import HttpResponseBase


class CreatePaymentUseCase(ABC):
    """
    CreatePaymentUseCase is an abstract class that defines the CreatePaymentUseCase interface.

    Attributes
    ----------
    None

    Methods
    -------
    create(payment_data)
        Create a payment.
    """
    @abstractmethod
    def create(self, payment_data: dict)-> HttpResponseBase:
        """Create a payment.

        Parameters
        ----------
        payment_data : dict
            The payment data.

        Returns
        -------
        HttpResponseBase
            The response.
        """
        pass