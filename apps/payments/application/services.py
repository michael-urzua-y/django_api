from apps.payments.persistence.repositories import PayinViewRepository, PayoutViewRepository

class PaymentService:
    def __init__(self):
        self.payin_repo = PayinViewRepository()
        self.payout_repo = PayoutViewRepository()

    def list_payins(self):
        return self.payin_repo.get_all()

    def list_payouts(self):
        return self.payout_repo.get_all()
