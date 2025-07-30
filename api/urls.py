from django.urls import path, include

urlpatterns = [
    path('payments/', include('apps.payments.presentation.urls')),
    path('users/', include('apps.users.presentation.urls')),  # 👈 Agrega esta línea
]
