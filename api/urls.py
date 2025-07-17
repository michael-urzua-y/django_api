from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')  # 👈 basename agregado

urlpatterns = [
    path('', include(router.urls)),
]
