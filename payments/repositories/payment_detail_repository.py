from abc import ABC, abstractmethod

from payments.models import PaymentDetail


class PaymentDetailRepository(ABC):
    """
    PaymentDetailRepository is an abstract class that defines the methods that
    any PaymentDetailRepository implementation must provide.
    
    Attributes
    ----------
    None
    
    Methods
    -------
    get_all()
        Get all payment details.
    get_by_external_id(external_id)
        Get a payment detail by external id.
    """
    @abstractmethod
    def get_all(self) -> list:
        """Get all payment details.
        
        Returns
        -------
        list
            A list of all payment details.
        """
        pass
    @abstractmethod
    def get_by_external_id(self, external_id: str)-> PaymentDetail:
        """Get a payment detail by external id.

        Parameters
        ----------
        external_id : str
            The external id of the payment detail to get.

        Returns
        -------
        PaymentDetail
            The payment detail with the given external id.
        """
        pass