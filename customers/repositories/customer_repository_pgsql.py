from django.shortcuts import get_object_or_404

from customers.models import Customer
from customers.repositories.customer_repository import CustomerRepository


class CustomerRepositoryPgsql(CustomerRepository):
    """
    CustomerRepositoryPgsql is a class that implements the CustomerRepository abstract class.

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
    def get_all(self):
        """Get all customers.

        Returns
        -------
        list
            A list of all customers.
        """
        return Customer.objects.all()
    def get_by_external_id(self, external_id: str) -> Customer:
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
        return get_object_or_404(Customer, external_id=external_id)