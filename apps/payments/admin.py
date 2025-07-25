from django.contrib import admin
from apps.payments.domain.models import Currency, Commission,Payin,PayinTrace

admin.site.register(Currency, Commission,Payin,PayinTrace)
