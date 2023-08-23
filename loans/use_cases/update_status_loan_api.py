from typing import Any
from datetime import datetime

from rest_framework import status
from rest_framework.response import Response

from loans.repositories.loan_repository import LoanRepository
from loans.repositories.loan_repository_pgsql import LoanRepositoryPgsql

from loans.helpers.outstanding import OutstandingHelper
from loans.serializers import LoanSerializer
from loans.use_cases.update_status_loan import UpdateStatusLoanUseCase


class UpdateStatusLoanApiUseCase(UpdateStatusLoanUseCase):
    """
    UpdateStatusLoanApiUseCase is a class that defines the UpdateStatusLoanApiUseCase interface.

    Attributes
    ----------
    loan_repository : LoanRepository
        The loan repository.
    outstanding_helper : OutstandingHelper
        The outstanding helper.

    Methods
    -------
    update(external_id, loan_status)
        Update the status of a loan.
    """
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.loan_repository: LoanRepository = LoanRepositoryPgsql()
        self.outstanding_helper = OutstandingHelper()

    def update(self, external_id: str, loan_status: int)-> Response:
        """Update the status of a loan.

        Parameters
        ----------
        external_id : str
            The external id of the loan to update the status.
        loan_status : int
            The status of the loan to update.

        Returns
        -------
        Response
            The response of the request.
        """
        loan = self.loan_repository.get_by_external_id(external_id)
        if loan.status == 1 and loan_status == 2:
            if self.outstanding_helper.calculate(loan.customer.id) + loan.outstanding > loan.customer.score:
                return Response({"error": "loan outstanding exceeds customer score"}, status=status.HTTP_400_BAD_REQUEST)
            loan.status = 2
            loan.taken_at = datetime.now()
            loan.save()
            serializer = LoanSerializer(loan)
            return Response(serializer.data)
        elif loan.status == 1 and loan_status == 3:
            loan.status = 3
            loan.save()
            serializer = LoanSerializer(loan)
            return Response(serializer.data)
        else:
            return Response({"error": "loan status cannot be updated"}, status=status.HTTP_400_BAD_REQUEST)