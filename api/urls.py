from django.urls import path, include

urlpatterns = [
    path('users/', include('apps.users.presentation.urls')),
    path('products/', include('apps.products.presentation.urls')),
]


