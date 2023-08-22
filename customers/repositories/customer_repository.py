from abc import ABC, abstractmethod

from customers.models import Customer


class CustomerRepository(ABC):
    """
    CustomerRepository is an abstract class that defines the CustomerRepository interface.

    Attributes
    ----------
    None

    Methods
    -------
    get_all()
        Get all customers.
    get_by_external_id(external_id)
        Get a customer by external id.
    """
    @abstractmethod
    def get_all(self) -> list:
        """Get all customers.

        Returns
        -------
        list
            A list of all customers.
        """
        pass
    @abstractmethod
    def get_by_external_id(self, external_id: str)-> Customer:
        """Get a customer by external id.

        Parameters
        ----------
        external_id : str
            The external id of the customer to get.

        Returns
        -------
        Customer
            The customer with the given external id.
        """
        pass