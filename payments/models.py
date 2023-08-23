from django.db import models

# Create your models here.
class Payment(models.Model):
    """
    Payment model

    Fields:
        created_at (DateTimeField): Date and time of creation
        updated_at (DateTimeField): Date and time of last update
        external_id (CharField): External id of the payment
        total_amount (DecimalField): Total amount of the payment
        status (SmallIntegerField): Status of the payment
        paid_at (DateTimeField): Date and time of the payment paid
        customer (ForeignKey): Customer of the payment
    """
    ESTATUSES = (
        (1, 'completed'),
        (2, 'rejected'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=60, unique=True)
    total_amount = models.DecimalField(max_digits=20, decimal_places=10)
    status = models.SmallIntegerField(choices=ESTATUSES, null=True, blank=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE, related_name='payments')

class PaymentDetail(models.Model):
    """
    PaymentDetail model
    
    Fields:
        created_at (DateTimeField): Date and time of creation
        updated_at (DateTimeField): Date and time of last update
        amount (DecimalField): Amount of the payment detail
        loan (ForeignKey): Loan of the payment detail
        payment (ForeignKey): Payment of the payment detail
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    loan = models.ForeignKey('loans.Loan', on_delete=models.CASCADE, related_name='payment_details')
    payment = models.ForeignKey('payments.Payment', on_delete=models.CASCADE, related_name='payment_details')
