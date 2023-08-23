from django.shortcuts import get_object_or_404

from payments.models import Payment
from payments.repositories.payment_repository import PaymentRepository


class PaymentRepositoryPgsql(PaymentRepository):
    """
    PaymentRepositoryPgsql is a class used to handle the payments in the database.

    Attributes
    ----------
    None

    Methods
    -------
    get_all()
        Get all payments.
    get_by_external_id(external_id)
        Get a payment by external id.
    """
    def get_all(self):
        """Get all payments.

        Returns
        -------
        list
            A list of all payments.
        """
        return Payment.objects.all()
    def get_by_external_id(self, external_id: str) -> Payment:
        """Get a payment by external id.

        Parameters
        ----------
        external_id : str
            The external id of the payment to get.
            
        Returns
        -------
        Payment
            The payment with the given external id.
        """
        return get_object_or_404(Payment, external_id=external_id)