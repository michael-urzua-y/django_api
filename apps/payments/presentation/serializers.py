
from rest_framework import serializers
from apps.payments.domain.payin_view_model import PayinView
from apps.payments.domain.payout_view_model import PayoutView

class PayinViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayinView
        fields = '__all__'

class PayoutViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayoutView
        fields = '__all__'
