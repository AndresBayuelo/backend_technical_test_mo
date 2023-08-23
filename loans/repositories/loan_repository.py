from abc import ABC, abstractmethod

from loans.models import Loan


class LoanRepository(ABC):
    """
    LoanRepository is an abstract class that defines the LoanRepository interface.

    Attributes
    ----------
    None

    Methods
    -------
    get_all()
        Get all loans.
    get_by_external_id(external_id)
        Get a loan by external id.
    """
    @abstractmethod
    def get_all(self) -> list:
        """Get all loans.
        
        Returns
        -------
        list
            A list of all loans.
        """
        pass
    @abstractmethod
    def get_by_external_id(self, external_id: str)-> Loan:
        """Get a loan by external id.

        Parameters
        ----------
        external_id : str
            The external id of the loan to get.

        Returns
        -------
        Loan
            The loan with the given external id.
        """
        pass