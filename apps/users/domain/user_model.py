from django.db import models
from apps.users.domain.commerce_model import Commerce

class User(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    commerce = models.ForeignKey(Commerce, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=255, null=True)
    ip = models.GenericIPAddressField(null=True)
    role = models.CharField(max_length=50, null=True)
    permissions = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'user'
