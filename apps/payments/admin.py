from django.contrib import admin
from apps.payments.domain.models_model import Currency, Commission,Payin,PayinTrace

admin.site.register(Currency, Commission,Payin,PayinTrace)
