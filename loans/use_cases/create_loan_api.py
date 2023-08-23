from decimal import Decimal
from typing import Any

from rest_framework import status
from rest_framework.response import Response

from customers.repositories.customer_repository import CustomerRepository
from customers.repositories.customer_repository_pgsql import \
    CustomerRepositoryPgsql
from loans.helpers.outstanding import OutstandingHelper
from loans.serializers import LoanSerializer
from loans.use_cases.create_loan import CreateLoanUseCase


class CreateLoanApiUseCase(CreateLoanUseCase):
    """
    CreateLoanApiUseCase is a class that defines the CreateLoanApiUseCase interface.

    Attributes
    ----------
    customer_repository : CustomerRepository
        The customer repository.
    outstanding_helper : OutstandingHelper
        The outstanding helper.

    Methods
    -------
    create(loan_data)
        Create a loan.
    """
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.customer_repository: CustomerRepository = CustomerRepositoryPgsql()
        self.outstanding_helper = OutstandingHelper()

    def create(self, loan_data: dict)-> Response:
        """Create a loan.

        Parameters
        ----------
        loan_data : dict
            The data of the loan to create.

        Returns
        -------
        Response
            The response of the request.
        """
        customer = self.customer_repository.get_by_external_id(loan_data['customer_external_id'])
        
        if customer.status == 2:
            return Response({"error": "customer is blacklisted"}, status=status.HTTP_400_BAD_REQUEST)
        
        if (self.outstanding_helper.calculate(customer.id) + Decimal(loan_data['outstanding'])) > customer.score:
            return Response({"error": "loan outstanding exceeds customer score"}, status=status.HTTP_400_BAD_REQUEST)
        
        loan_data['customer'] = customer.id
        del loan_data['customer_external_id']
        del loan_data['status']
        
        serializer = LoanSerializer(data=loan_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_200_OK)