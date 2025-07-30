from django.db import models

class PayoutView(models.Model):
    referencia = models.CharField(max_length=100)
    usuario = models.CharField(max_length=255)
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    comercio = models.CharField(max_length=255)
    moneda = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'payout_view'
