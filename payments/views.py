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
from payments.repositories.payment_repository import PaymentRepository
from payments.repositories.payment_repository_pgsql import \
    PaymentRepositoryPgsql
from payments.use_cases.create_payment import CreatePaymentUseCase
from payments.use_cases.create_payment_api import CreatePaymentApiUseCase
from payments.use_cases.update_status_payment import UpdateStatusPaymentUseCase
from payments.use_cases.update_status_payment_api import \
    UpdateStatusPaymentApiUseCase

from .serializers import PaymentSerializer


# Create your views here.
class PaymentViewSet(viewsets.ViewSet):
    """
    PaymentViewSet is a class that defines the PaymentViewSet interface.

    Attributes
    ----------
    customer_repository : CustomerRepository
        The customer repository.
    payment_repository : PaymentRepository
        The payment repository.
    create_payment_use_case : CreatePaymentUseCase
        The create payment use case.
    update_status_payment_use_case : UpdateStatusPaymentUseCase
        The update status payment use case.
    
    Methods
    -------
    list(request)
        List all payments.
    retrieve(request, pk=None)
        Get a payment by external id.
    get_by_customer(request)
        Get all payments of a customer.
    create(request)
        Create a payment.
    update_status(request, pk=None)
        Update the status of a payment.
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.create_payment_use_case: CreatePaymentUseCase = CreatePaymentApiUseCase()
        self.update_status_payment_use_case: UpdateStatusPaymentUseCase = UpdateStatusPaymentApiUseCase()
        self.payment_repository: PaymentRepository = PaymentRepositoryPgsql()
        self.customer_repository: CustomerRepository = CustomerRepositoryPgsql()

    def list(self, request)-> Response:
        """ List all payments.
        
        Parameters
        ----------
        request
            The request.

        Returns
        -------
        Response
            The response of the request.
        """
        payments = self.payment_repository.get_all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None)-> Response:
        """ Get a payment by external id.

        Parameters
        ----------
        request
            The request.
        pk : str
            The external id of the payment.

        Returns
        -------
        Response
            The response of the request.
        """

        payment = self.payment_repository.get_by_external_id(pk)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)
    
    @action(
        methods=['get'], 
        detail=False,
    )
    def get_by_customer(self, request)-> Response:
        """ Get all payments of a customer.

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
        payments = self.payment_repository.get_all().filter(customer_id=customer.id)
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def create(self, request)-> Response:
        """ Create a payment.

        Parameters
        ----------
        request
            The request.

        Returns
        -------
        Response
            The response of the request.
        """
        return self.create_payment_use_case.create(request.data)
    
    @action(
        methods=['patch'], 
        detail=True,
    )
    def update_status(self, request, pk=None)-> Response:
        """ Update the status of a payment.

        Parameters
        ----------
        request
            The request.
        pk : str
            The external id of the payment.

        Returns
        -------
        Response
            The response of the request.
        """
        return self.update_status_payment_use_case.update(pk, request.data['status'])