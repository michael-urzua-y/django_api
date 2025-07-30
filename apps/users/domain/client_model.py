from django.db import models
from .commerce_model import Commerce
from .country_model import Country
from .document_type_model import DocumentType

class Client(models.Model):
    client_id = models.CharField(max_length=10, primary_key=True)
    commerce = models.ForeignKey(Commerce, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    document = models.CharField(max_length=20)
    document_format = models.CharField(max_length=10)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    blocked = models.BooleanField()
    blocked_restriction = models.CharField(max_length=100, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'client'