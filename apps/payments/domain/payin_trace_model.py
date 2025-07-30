from django.db import models
from .payin_model import Payin
from apps.products.domain.models import InternalState

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

    class Meta:
        db_table = 'payin_trace'