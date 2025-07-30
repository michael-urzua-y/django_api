from apps.payments.domain.payin_view_model import PayinView
from apps.payments.domain.payout_view_model import PayoutView

class PayinViewRepository:
    def get_all(self):
        return PayinView.objects.all()

class PayoutViewRepository:
    def get_all(self):
        return PayoutView.objects.all()
