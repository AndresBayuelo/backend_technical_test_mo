from abc import ABC, abstractmethod

from django.http import HttpResponseBase


class CreateLoanUseCase(ABC):
    """
    CreateLoanUseCase is an abstract class that defines the CreateLoanUseCase interface.
    
    Attributes
    ----------
    None
    
    Methods
    -------
    create(loan_data)
        Create a loan.
    """
    @abstractmethod
    def create(self, loan_data: dict)-> HttpResponseBase:
        """Create a loan.

        Parameters
        ----------
        loan_data : dict
            The data of the loan to create.

        Returns
        -------
        HttpResponseBase
            The response of the request.
        """
        pass