# from django.db import models

# class User(models.Model):
#     id = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     direccion = models.TextField(null=True, blank=True)
#     comuna = models.TextField(null=True, blank=True)
#     pais = models.TextField(null=True, blank=True)

#     class Meta:
#         db_table = '"api_users"."users"'  # Referencia al esquema y tabla en la base de datos
#         managed = False             # Django no gestionará esta tabla
#     def __str__(self):
#         return self.nombre


from django.db import models

class DocumentType(models.Model):
    document_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = '"prontopaga"."document_type"'
        managed = False

class Country(models.Model):
    country_id = models.CharField(max_length=10, primary_key=True)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = '"prontopaga"."countrys"'
        managed = False

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
        db_table = '"prontopaga"."commerce"'
        managed = False

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
        db_table = '"prontopaga"."client"'
        managed = False

class User(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    commerce = models.ForeignKey(Commerce, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    ip = models.GenericIPAddressField()
    role = models.CharField(max_length=50)
    permissions = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = '"prontopaga"."user"'
        managed = False
