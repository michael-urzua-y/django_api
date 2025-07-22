from django.db import models

class User(models.Model):
    
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    direccion = models.TextField(null=True, blank=True)
    comuna = models.TextField(null=True, blank=True)
    pais = models.TextField(null=True, blank=True)


    class Meta:
        db_table = '"api"."users"'  # Esquema y tabla correctamente referenciados
        managed = False             # Django no gestionará la creación/modificación de esta tabla

    def __str__(self):
        return self.nombre
