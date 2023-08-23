from rest_framework import serializers
from .models import Payment, PaymentDetail

class PaymentDetailSerializer(serializers.ModelSerializer):
    loan_external_id = serializers.StringRelatedField(source='loan.external_id')
    payment_external_id = serializers.StringRelatedField(source='payment.external_id')

    class Meta:
        model = PaymentDetail
        fields = ['payment_external_id', 'payment', 'loan_external_id', 'loan', 'amount']
        extra_kwargs = {
            'payment': {'write_only': True},
            'loan': {'write_only': True},
        }

class PaymentSerializer(serializers.ModelSerializer):
    customer_external_id = serializers.StringRelatedField(source='customer.external_id')
    payment_details = PaymentDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Payment
        fields = ['external_id', 'customer_external_id', 'customer', 'total_amount', 'status', 'paid_at', 'payment_details']
        extra_kwargs = {
            'customer': {'write_only': True},
        }