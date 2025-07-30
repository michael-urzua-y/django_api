from django.db import models
from .currency_model import Currency
from .commission_model import Commission
from apps.users.domain.client_model import Client
from apps.users.domain.country_model import Country
from apps.products.domain.models import Type, Method, Status

class Payin(models.Model):
    transaction_id = models.CharField(max_length=20, primary_key=True)
    currency = models.ForeignKey(Currency, to_field='currency_id', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    client_email_id = models.CharField(max_length=100, null=True, blank=True)
    client_phone_id = models.CharField(max_length=100, null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    statu = models.ForeignKey(Status, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    real_amount = models.DecimalField(max_digits=10, decimal_places=2)
    token_ws = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    commentary = models.TextField()
    url_confirmation = models.URLField()
    url_final = models.URLField()
    metadata = models.JSONField()
    note = models.TextField()
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE)
    code_response_webhook = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)
