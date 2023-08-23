from rest_framework import serializers
from .models import Loan

class LoanSerializer(serializers.ModelSerializer):
    customer_external_id = serializers.StringRelatedField(source='customer.external_id')

    class Meta:
        model = Loan
        fields = ['external_id', 'customer_external_id', 'customer', 'amount', 'outstanding', 'status', 'taken_at']
        extra_kwargs = {
            'customer': {'write_only': True},
        }
