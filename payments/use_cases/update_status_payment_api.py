from datetime import datetime
from typing import Any

from rest_framework import status
from rest_framework.response import Response

from loans.repositories.loan_repository import LoanRepository
from loans.repositories.loan_repository_pgsql import LoanRepositoryPgsql
from payments.repositories.payment_detail_repository import \
    PaymentDetailRepository
from payments.repositories.payment_detail_repository_pgsql import \
    PaymentDetailRepositoryPgsql
from payments.repositories.payment_repository import PaymentRepository
from payments.repositories.payment_repository_pgsql import \
    PaymentRepositoryPgsql
from payments.serializers import PaymentSerializer
from payments.use_cases.update_status_payment import UpdateStatusPaymentUseCase


class UpdateStatusPaymentApiUseCase(UpdateStatusPaymentUseCase):
    """
    UpdateStatusPaymentApiUseCase is a class that defines the UpdateStatusPaymentApiUseCase interface.

    Attributes
    ----------
    payment_repository : PaymentRepository
        The payment repository.
    payment_detail_repository : PaymentDetailRepository
        The payment detail repository.
    loan_repository : LoanRepository
        The loan repository.

    Methods
    -------
    update(external_id, payment_status)
        Update the status of a payment.
    """
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.payment_repository: PaymentRepository = PaymentRepositoryPgsql()
        self.payment_detail_repository: PaymentDetailRepository = PaymentDetailRepositoryPgsql()
        self.loan_repository: LoanRepository = LoanRepositoryPgsql()

    def update(self, external_id: str, payment_status: int)-> Response:
        """ Update the status of a payment.

        Parameters
        ----------
        external_id : str
            The external id of the payment.
        payment_status : int
            The status of the payment.

        Returns
        -------
        Response
            The response.
        """
        payment = self.payment_repository.get_by_external_id(external_id)
        if payment.status is None and payment_status == 1:
            payment_details = self.payment_detail_repository.get_all().filter(payment=payment.id)
            for detail in payment_details:
                loan = self.loan_repository.get_by_external_id(detail.loan.external_id)
                if loan.status != 2:
                    return Response({"error": "loan is not active"}, status=status.HTTP_400_BAD_REQUEST)
                if loan.outstanding < detail.amount:
                    return Response({"error": "payment amount exceeds loan outstanding"}, status=status.HTTP_400_BAD_REQUEST)
                
            for detail in payment_details:
                loan = self.loan_repository.get_by_external_id(detail.loan.external_id)
                loan.outstanding -= detail.amount
                loan.status = 4 if loan.outstanding == 0 else loan.status
                loan.save()

            payment.status = 1
            payment.paid_at = datetime.now()
            payment.save()
            serializer = PaymentSerializer(payment)
            return Response(serializer.data)
        
        elif payment.status is None and payment_status == 2:
            payment.status = 2
            payment.save()
            serializer = PaymentSerializer(payment)
            return Response(serializer.data)
        
        else:
            return Response({"error": "loan status cannot be updated"}, status=status.HTTP_400_BAD_REQUEST)