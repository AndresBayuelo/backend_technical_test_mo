from abc import ABC, abstractmethod

from django.http import HttpResponseBase


class CreateCustomerUseCase(ABC):
    """
    CreateCustomerUseCase is an abstract class that defines the CreateCustomerUseCase interface.

    Attributes
    ----------
    None

    Methods
    -------
    create(customer_data)
        Create a customer.
    """
    @abstractmethod
    def create(self, customer_data: dict)-> HttpResponseBase:
        """Create a customer.
        
        Parameters
        ----------
        customer_data : dict
            The data of the customer to create.

        Returns
        -------
        HttpResponseBase
            The response of the creation.    
        """
        pass