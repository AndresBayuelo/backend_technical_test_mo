from abc import ABC, abstractmethod

from django.http import HttpResponseBase


class UpdateStatusLoanUseCase(ABC):
    """
    UpdateStatusLoanUseCase is an abstract class that defines the UpdateStatusLoanUseCase interface.

    Attributes
    ----------
    None

    Methods
    -------
    update(external_id, status)
        Update the status of a loan.
    """
    @abstractmethod
    def update(self, external_id: str, status: int)-> HttpResponseBase:
        """Update the status of a loan.

        Parameters
        ----------
        external_id : str
            The external id of the loan to update the status.
        status : int
            The status of the loan to update.

        Returns
        -------
        HttpResponseBase
            The response of the request.
        """
        pass