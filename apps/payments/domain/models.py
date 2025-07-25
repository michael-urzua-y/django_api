from django.db import models
from apps.products.domain.models import Type
from apps.products.domain.models import Isocode
from apps.products.domain.models import Status, Method
from apps.users.domain.models import Client
from apps.products.domain.models import InternalState
from apps.users.domain.models import Country

class Currency(models.Model):
    currency_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    isocode = models.ForeignKey(Isocode, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    ivapercent = models.DecimalField(max_digits=5, decimal_places=2)
    data_convert = models.JSONField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

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


class Payin(models.Model):
    transaction_id = models.CharField(max_length=20, primary_key=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
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


class PayinTrace(models.Model):
    id = models.AutoField(primary_key=True)
    transaction = models.ForeignKey(Payin, on_delete=models.CASCADE)
    request = models.JSONField()
    response = models.JSONField()
    internal_state = models.ForeignKey(InternalState, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)
