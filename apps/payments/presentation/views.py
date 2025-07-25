from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.payments.application.services import get_payment_report

class PaymentReportView(APIView):
    def post(self, request):
        esquema = request.data.get("esquema_bd")
        metodo = request.data.get("metodo")

        if not esquema or not metodo:
            return Response({"error": "esquema_bd y metodo son requeridos"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Pasar todo el request.data al service
            data = get_payment_report(request.data)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
