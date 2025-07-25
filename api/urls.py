from django.urls import path, include

urlpatterns = [
    path('payments/', include('apps.payments.presentation.urls')),
]
