from typing import Any

from rest_framework import viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from customers.repositories.customer_repository import CustomerRepository
from customers.repositories.customer_repository_pgsql import \
    CustomerRepositoryPgsql
from loans.repositories.loan_repository import LoanRepository
from loans.repositories.loan_repository_pgsql import LoanRepositoryPgsql
from loans.use_cases.create_loan import CreateLoanUseCase
from loans.use_cases.create_loan_api import CreateLoanApiUseCase
from loans.use_cases.update_status_loan import UpdateStatusLoanUseCase
from loans.use_cases.update_status_loan_api import UpdateStatusLoanApiUseCase

from .serializers import LoanSerializer


class LoanViewSet(viewsets.ViewSet):
    """
    LoanViewSet is a class that defines the LoanViewSet interface.

    Attributes
    ----------
    customer_repository : CustomerRepository
        The customer repository.
    loan_repository : LoanRepository
        The loan repository.
    create_loan_use_case : CreateLoanUseCase
        The create loan use case.
    update_status_loan_use_case : UpdateStatusLoanUseCase
        The update status loan use case.

    Methods
    -------
    list(request)
        List all loans.
    retrieve(request, pk=None)
        Get a loan by external id.
    get_by_customer(request)
        Get all loans of a customer.
    create(request)
        Create a loan.
    update_status(request, pk=None)
        Update the status of a loan.
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.customer_repository: CustomerRepository = CustomerRepositoryPgsql()
        self.loan_repository: LoanRepository = LoanRepositoryPgsql()
        self.create_loan_use_case: CreateLoanUseCase = CreateLoanApiUseCase()
        self.update_status_loan_use_case: UpdateStatusLoanUseCase = UpdateStatusLoanApiUseCase()

    def list(self, request)-> Response:
        """List all loans.

        Parameters
        ----------
        request
            The request.

        Returns
        -------
        Response
            The response of the request.
        """
        loans = self.loan_repository.get_all()
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None)-> Response:
        """Get a loan by external id.

        Parameters
        ----------
        request
            The request.
        pk : str
            The external id of the loan to get.

        Returns
        -------
        Response
            The response of the request.
        """
        loan = self.loan_repository.get_by_external_id(pk)
        serializer = LoanSerializer(loan)
        return Response(serializer.data)
    
    @action(
        methods=['get'], 
        detail=False,
    )
    def get_by_customer(self, request)-> Response:
        """Get all loans of a customer.

        Parameters
        ----------
        request
            The request.

        Returns
        -------
        Response
            The response of the request.
        """
        customer = self.customer_repository.get_by_external_id(request.query_params['customer_external_id'])
        loans = self.loan_repository.get_all().filter(customer_id=customer.id)
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)

    def create(self, request)-> Response:
        """Create a loan.

        Parameters
        ----------
        request
            The request.

        Returns
        -------
        Response
            The response of the request.
        """
        return self.create_loan_use_case.create(request.data)
    
    @action(
        methods=['patch'], 
        detail=True,
    )
    def update_status(self, request, pk=None)-> Response:
        """Update the status of a loan.

        Parameters
        ----------
        request
            The request.
        pk : str
            The external id of the loan to update the status.

        Returns
        -------
        Response
            The response of the request.
        """
        return self.update_status_loan_use_case.update(pk, request.data['status'])
    