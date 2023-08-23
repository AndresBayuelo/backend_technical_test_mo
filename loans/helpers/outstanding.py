from decimal import Decimal

from loans.repositories.loan_repository import LoanRepository
from loans.repositories.loan_repository_pgsql import LoanRepositoryPgsql

class OutstandingHelper:
    """
    This class is used to calculate the outstanding of a customer

    Attributes
    ----------
    loan_repository : LoanRepository
        The loan repository.

    Methods
    -------
    calculate(customer_id)
        Calculate the outstanding of a customer.
    """
    def __init__(self):
        self.loan_repository: LoanRepository = LoanRepositoryPgsql()

    def calculate(self, customer_id: int)-> Decimal:
        """Calculate the outstanding of a customer.
        
        Parameters
        ----------
        customer_id : int
            The id of the customer to calculate the outstanding.
            
        Returns
        -------
        Decimal
            The outstanding of the customer.
        """
        loans = self.loan_repository.get_all().filter(customer_id=customer_id)
        outstanding = 0
        for loan in loans:
            if loan.status == 2:
                outstanding += loan.outstanding
        return outstanding