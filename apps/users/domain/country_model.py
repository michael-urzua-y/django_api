from django.db import models

class Country(models.Model):
    country_id = models.CharField(max_length=10, primary_key=True)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'countrys'