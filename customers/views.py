from typing import Any

from rest_framework import viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .repositories.customer_repository import CustomerRepository
from .repositories.customer_repository_pgsql import CustomerRepositoryPgsql
from .serializers import CustomerSerializer
from .use_cases.create_customer import CreateCustomerUseCase
from .use_cases.create_customer_api import CreateCustomerApiUseCase


class CustomerViewSet(viewsets.ViewSet):
    """
    CustomerViewSet is a class that defines the CustomerViewSet interface.

    Attributes
    ----------
    customer_repository : CustomerRepository
        The customer repository.
    create_customer_use_case : CreateCustomerUseCase
        The create customer use case.

    Methods
    -------
    list(request)
        Get all customers.
    retrieve(request, pk=None)
        Get a customer by external id.
    create(request)
        Create a customer.
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.customer_repository: CustomerRepository = CustomerRepositoryPgsql()
        self.create_customer_use_case: CreateCustomerUseCase = CreateCustomerApiUseCase()

    def list(self, request)-> Response:
        """Get all customers.

        Returns
        -------
        Response
            The response of the request.
        """
        customers = self.customer_repository.get_all()
        return Response(CustomerSerializer(customers, many=True).data)
    
    def retrieve(self, request, pk=None)-> Response:
        """Get a customer by external id.

        Parameters
        ----------
        pk : str
            The external id of the customer to get.

        Returns
        -------
        Response
            The response of the request.
        """
        customer = self.customer_repository.get_by_external_id(pk)
        return Response(CustomerSerializer(customer).data)
    
    def create(self, request)-> Response:
        """Create a customer.

        Parameters
        ----------
        request : Request
            The request of the creation.

        Returns
        -------
        Response
           0 The response of the creation.
        """
        return self.create_customer_use_case.create(request.data)