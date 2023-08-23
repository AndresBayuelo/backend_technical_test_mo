from decimal import Decimal
from typing import Any

from rest_framework import status
from rest_framework.response import Response

from customers.repositories.customer_repository import CustomerRepository
from customers.repositories.customer_repository_pgsql import \
    CustomerRepositoryPgsql
from loans.repositories.loan_repository import LoanRepository
from loans.repositories.loan_repository_pgsql import LoanRepositoryPgsql
from payments.serializers import PaymentDetailSerializer, PaymentSerializer
from payments.use_cases.create_payment import CreatePaymentUseCase


class CreatePaymentApiUseCase(CreatePaymentUseCase):
    """
    CreatePaymentApiUseCase is a class that defines the CreatePaymentApiUseCase interface.

    Attributes
    ----------
    customer_repository : CustomerRepository
        The customer repository.
    loan_repository : LoanRepository
        The loan repository.

    Methods
    -------
    create(payment_data)
        Create a payment.
    """
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.customer_repository: CustomerRepository = CustomerRepositoryPgsql()
        self.loan_repository: LoanRepository = LoanRepositoryPgsql()

    def create(self, payment_data: dict)-> Response:
        """ Create a payment.

        Parameters
        ----------
        payment_data : dict
            The payment data.

        Returns
        -------
        Response
            The response.
        """
        customer = self.customer_repository.get_by_external_id(payment_data['customer_external_id'])
        for datail in payment_data['details']:
            loan = self.loan_repository.get_by_external_id(datail['loan_external_id'])
            if loan.customer.id != customer.id:
                return Response({"error": "loan does not belong to customer"}, status=status.HTTP_400_BAD_REQUEST)
            if loan.status != 2:
                return Response({"error": "loan is not active"}, status=status.HTTP_400_BAD_REQUEST)
            if loan.outstanding < datail['amount']:
                return Response({"error": "payment amount exceeds loan outstanding"}, status=status.HTTP_400_BAD_REQUEST)
            
        paymentSerializer = PaymentSerializer(data={
            "external_id": payment_data['external_id'],
            "customer": customer.id,
            "total_amount": 0.0,
        })
        if paymentSerializer.is_valid():
            payment = paymentSerializer.save()
            
            paymentDetails = []
            for datail in payment_data['details']:
                loan = self.loan_repository.get_by_external_id(datail['loan_external_id'])
                paymentDetailSerializer = PaymentDetailSerializer(data={
                    "payment": payment.id,
                    "loan": loan.id,
                    "amount": datail['amount'],
                })
                if paymentDetailSerializer.is_valid():
                    paymentDetailSerializer.save()
                    payment.total_amount += Decimal(datail['amount'])
                    paymentDetails.append(paymentDetailSerializer.data)
                else:
                    return Response(paymentDetailSerializer.errors, status=status.HTTP_200_OK)
            
            payment.save()
            
            paymentData = paymentSerializer.data
            paymentData['total_amount'] = payment.total_amount
            paymentData['details'] = paymentDetails
            return Response(paymentData)
        
        return Response(paymentSerializer.errors, status=status.HTTP_200_OK)