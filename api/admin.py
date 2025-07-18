from django.contrib import admin
from .models import User, Product  # Importa los modelos desde __init__.py

admin.site.register(User)
admin.site.register(Product)
