from abc import ABC, abstractmethod

from payments.models import Payment


class PaymentRepository(ABC):
    """
    PaymentRepository is an abstract class that defines the methods that
    any PaymentRepository implementation must provide.

    Attributes
    ----------
    None

    Methods
    -------
    get_all()
        Get all payments.
    get_by_external_id(external_id)
        Get a payment by external id.
    """
    @abstractmethod
    def get_all(self) -> list:
        """Get all payments.

        Returns
        -------
        list
            A list of all payments.
        """
        pass
    @abstractmethod
    def get_by_external_id(self, external_id: str)-> Payment:
        """Get a payment by external id.

        Parameters
        ----------
        external_id : str
            The external id of the payment to get.

        Returns
        -------
        Payment
            The payment with the given external id.
        """
        pass