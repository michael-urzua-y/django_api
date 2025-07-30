from django.db import models

class PayinView(models.Model):
    referencia = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=255)
    estado = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    metodo = models.CharField(max_length=100)
    comercio = models.CharField(max_length=255)
    moneda = models.CharField(max_length=50)
    creado = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payin_view'
