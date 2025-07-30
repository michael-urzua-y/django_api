from django.db import models
from .currency_model import Currency
from apps.products.domain.models import Type

class Commission(models.Model):
    commission_id = models.CharField(max_length=10, primary_key=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    ivaamount = models.DecimalField(max_digits=10, decimal_places=2)
    ivapercent = models.DecimalField(max_digits=5, decimal_places=2)
    percent = models.DecimalField(max_digits=5, decimal_places=2)
    commission_total = models.DecimalField(max_digits=10, decimal_places=2)
    iva_total = models.DecimalField(max_digits=10, decimal_places=2)
    minimun_rate = models.DecimalField(max_digits=10, decimal_places=2)
    iva_minimun_rate = models.DecimalField(max_digits=10, decimal_places=2)
    flate_rate = models.DecimalField(max_digits=10, decimal_places=2)
    iva_flate_rate = models.DecimalField(max_digits=10, decimal_places=2)
    applied_rate = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'commissions'
