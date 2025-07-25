# from django.db import models

# class Product(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.IntegerField()

#     class Meta:
#         db_table = '"api_products"."products"'  # Esquema y tabla correctamente referenciados
#         managed = False                # Django no gestionará la tabla

#     def __str__(self):
#         return self.name

from django.db import models

class Isocode(models.Model):
    isocode_id = models.CharField(max_length=10, primary_key=True)
    isocode = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = '"prontopaga"."isocodes"'
        managed = False

class Type(models.Model):
    type_id = models.CharField(max_length=10, primary_key=True)
    type = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = '"prontopaga"."types"'
        managed = False

class Method(models.Model):
    method_id = models.CharField(max_length=10, primary_key=True)
    method = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = '"prontopaga"."methods"'
        managed = False

class Status(models.Model):
    statu_id = models.CharField(max_length=10, primary_key=True)
    statu = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = '"prontopaga"."status"'
        managed = False

class ExternalState(models.Model):
    id = models.AutoField(primary_key=True)
    external_state = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = '"prontopaga"."external_state"'
        managed = False

class InternalState(models.Model):
    id = models.AutoField(primary_key=True)
    external_state = models.ForeignKey(ExternalState, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = '"prontopaga"."internal_state"'
        managed = False
