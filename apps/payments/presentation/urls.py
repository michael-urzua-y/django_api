from django.urls import path
from .views import PayinViewList, PayoutViewList

urlpatterns = [
    path('payins/', PayinViewList.as_view(), name='payin-view-list'),
    path('payouts/', PayoutViewList.as_view(), name='payout-view-list'),
]
