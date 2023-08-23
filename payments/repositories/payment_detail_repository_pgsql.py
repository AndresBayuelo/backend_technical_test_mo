from django.shortcuts import get_object_or_404

from payments.models import PaymentDetail
from payments.repositories.payment_detail_repository import \
    PaymentDetailRepository


class PaymentDetailRepositoryPgsql(PaymentDetailRepository):
    """
    PaymentDetailRepositoryPgsql is a class used to handle the payment details
    in the database.

    Attributes
    ----------
    None

    Methods
    -------
    get_all()
        Get all payment details.
    get_by_external_id(external_id)
        Get a payment detail by external id.
    """
    def get_all(self):
        """Get all payment details.

        Returns
        -------
        list
            A list of all payment details.
        """
        return PaymentDetail.objects.all()
    def get_by_external_id(self, external_id: str) -> PaymentDetail:
        """Get a payment detail by external id.

        Parameters
        ----------
        external_id : str
            The external id of the payment detail to get.
        
        Returns
        -------
        PaymentDetail
            The payment detail with the given external id.
        """
        return get_object_or_404(PaymentDetail, external_id=external_id)