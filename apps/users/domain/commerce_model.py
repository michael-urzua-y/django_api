from django.db import models

class Commerce(models.Model):
    commerce_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=20)
    document_format = models.CharField(max_length=10)
    iso_code = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'commerce'
