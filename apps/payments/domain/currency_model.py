from django.db import models
from apps.products.domain.models import Type, Isocode
from apps.users.domain.country_model import Country

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
    
    class Meta:
        db_table = 'currency'
