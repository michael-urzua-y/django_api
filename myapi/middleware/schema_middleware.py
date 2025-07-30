# myapi/middleware/schema_middleware.py

from django.db import connection
from django.utils.deprecation import MiddlewareMixin
from myapi.esquemas import SCHEMA_MAP

class SchemaMiddleware(MiddlewareMixin):
    def process_request(self, request):
        schema_key = request.GET.get('schema')
        if schema_key:
            schema_name = SCHEMA_MAP.get(schema_key)
            if not schema_name:
                raise ValueError(f"Esquema '{schema_key}' no está definido en SCHEMA_MAP.")
            with connection.cursor() as cursor:
                cursor.execute(f'SET search_path TO {schema_name}')
