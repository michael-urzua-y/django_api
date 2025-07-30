#Este archivo puede ser útil si estás organizando las rutas por módulos o apps 
#(como users, payments, etc.), pero no tiene efecto si no está incluido en myapi/urls.py.

from django.urls import path, include

urlpatterns = [
    path('users/', include('apps.users.presentation.urls')),
    path('payments/', include('apps.payments.presentation.urls')),
]
