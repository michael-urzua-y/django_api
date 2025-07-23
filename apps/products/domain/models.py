from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    class Meta:
        db_table = '"api"."products"'  # Esquema y tabla correctamente referenciados
        managed = False                # Django no gestionará la tabla

    def __str__(self):
        return self.name
