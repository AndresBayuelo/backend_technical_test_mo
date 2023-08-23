from django.shortcuts import get_object_or_404

from loans.models import Loan
from loans.repositories.loan_repository import LoanRepository


class LoanRepositoryPgsql(LoanRepository):
    def get_all(self):
        return Loan.objects.all()
    def get_by_external_id(self, external_id: str) -> Loan:
        return get_object_or_404(Loan, external_id=external_id)