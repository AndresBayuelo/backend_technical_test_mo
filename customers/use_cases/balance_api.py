from typing import Any

from rest_framework.response import Response

from customers.repositories.customer_repository import CustomerRepository
from customers.repositories.customer_repository_pgsql import \
    CustomerRepositoryPgsql
from customers.use_cases.balance import BalanceUseCase
from loans.helpers.outstanding import OutstandingHelper


class BalanceApiUseCase(BalanceUseCase):
    """
    BalanceApiUseCase is a class that defines the BalanceApiUseCase interface.

    Attributes
    ----------
    customer_repository : CustomerRepository
        The customer repository.
    outstanding_helper : OutstandingHelper
        The outstanding helper.

    Methods
    -------
    get(external_id)
        Get the balance of a customer.
    """
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.customer_repository: CustomerRepository = CustomerRepositoryPgsql()
        self.outstanding_helper = OutstandingHelper()

    def get(self, external_id: str) -> Response:
        """Get the balance of a customer.

        Parameters
        ----------
        external_id : str
            The external id of the customer to get the balance.

        Returns
        -------
        Response
            The response of the request.
        """
        customer = self.customer_repository.get_by_external_id(external_id)
        outstanding = self.outstanding_helper.calculate(customer.id)
        return Response({
            "external_id": customer.external_id,
            "score": customer.score,
            "avalaible_amount": customer.score - outstanding,
            "total_debt": outstanding,
        })