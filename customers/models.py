from django.db import models

# Create your models here.
class Customer(models.Model):
    """
    Customer model

    Fields:
        created_at (DateTimeField): Date and time of creation
        updated_at (DateTimeField): Date and time of last update
        external_id (CharField): External id of the customer
        status (SmallIntegerField): Status of the customer
        score (DecimalField): Score of the customer
        preapproved_at (DateTimeField): Date and time of the preapproved
        
    """
    ESTATUSES = (
        (1, 'Activo'),
        (2, 'Inactivo'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=60, unique=True)
    status = models.SmallIntegerField(choices=ESTATUSES, default=1)
    score = models.DecimalField(max_digits=10, decimal_places=2)
    preapproved_at = models.DateTimeField(null=True, blank=True)
