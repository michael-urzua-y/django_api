from django.urls import path
from .views import PaymentReportView

urlpatterns = [
    path('payments/', PaymentReportView.as_view(), name='payment-report'),
]
