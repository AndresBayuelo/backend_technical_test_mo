from django.db import models

# Create your models here.
class Loan(models.Model):
    """
    Loan model
    
    Fields:
        created_at (DateTimeField): Date and time of creation
        updated_at (DateTimeField): Date and time of last update
        external_id (CharField): External id of the loan
        amount (DecimalField): Amount of the loan
        status (SmallIntegerField): Status of the loan
        contract_version (CharField): Contract version of the loan
        maximum_payment_date (DateTimeField): Maximum payment date of the loan
        taken_at (DateTimeField): Date and time of the loan taken
        customer (ForeignKey): Customer of the loan
        outstanding (DecimalField): Outstanding of the loan
        
    """
    ESTATUSES = (
        (1, 'pending'),
        (2, 'active'),
        (3, 'rejected'),
        (4, 'paid'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=60, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.SmallIntegerField(choices=ESTATUSES, default=1)
    contract_version = models.CharField(max_length=30, null=True, blank=True)
    maximum_payment_date = models.DateTimeField(null=True, blank=True)
    taken_at = models.DateTimeField(null=True, blank=True)
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE, related_name='loans')
    outstanding = models.DecimalField(max_digits=10, decimal_places=2)
