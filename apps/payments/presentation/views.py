from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.payments.application.services import PaymentService
from apps.payments.presentation.serializers import PayinViewSerializer, PayoutViewSerializer

class PayinViewList(APIView):
    def get(self, request):
        service = PaymentService()
        queryset = service.list_payins()
        serializer = PayinViewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PayoutViewList(APIView):
    def get(self, request):
        service = PaymentService()
        queryset = service.list_payouts()
        serializer = PayoutViewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
