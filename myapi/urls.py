# Este archivo es el que Django usa como punto de entrada para todas las URLs. 
# Aquí es donde se deben incluir las rutas de todas las apps del proyecto,
# normalmente bajo prefijos como /api/, /admin/, etc.
#✅ Este archivo es el que debes modificar para que tus vistas estén disponibles en Postman.

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Mi API",
        default_version='v1',
        description="Documentación de la API de usuarios y pagos",
        terms_of_service="",
        contact=openapi.Contact(email="tu-email@ejemplo.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # 👈 Centraliza todas las rutas de apps
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
