from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    direccion = models.TextField(null=True, blank=True)
    comuna = models.TextField(null=True, blank=True)
    pais = models.TextField(null=True, blank=True)

    class Meta:
        db_table = '"api"."users"'  # Referencia al esquema y tabla en la base de datos
        managed = False             # Django no gestionará esta tabla
    def __str__(self):
        return self.nombre
