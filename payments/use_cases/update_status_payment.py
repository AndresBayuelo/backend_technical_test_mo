from abc import ABC, abstractmethod

from django.http import HttpResponseBase


class UpdateStatusPaymentUseCase(ABC):
    """
    UpdateStatusPaymentUseCase is an abstract class that defines the UpdateStatusPaymentUseCase interface.

    Attributes
    ----------
    None

    Methods
    -------
    update(external_id, status)
        Update a payment status.
    """
    @abstractmethod
    def update(self, external_id: str, status: int)-> HttpResponseBase:
        pass