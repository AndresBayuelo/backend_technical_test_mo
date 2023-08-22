from rest_framework import status
from rest_framework.response import Response

from customers.serializers import CustomerSerializer
from customers.use_cases.create_customer import CreateCustomerUseCase


class CreateCustomerApiUseCase(CreateCustomerUseCase):
    """
    CreateCustomerApiUseCase is a class that implements the CreateCustomerUseCase abstract class.
    """
    def create(self, customer_data: dict)-> Response:
        """Create a customer.
        
        Parameters
        ----------
        customer_data : dict
            The data of the customer to create.

        Returns
        -------
        Response
            The response of the creation.    
        """
        serializer = CustomerSerializer(data=customer_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_200_OK)