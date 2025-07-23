from rest_framework.routers import DefaultRouter
from apps.users.presentation.views import UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')  # sin prefijo adicional

urlpatterns = router.urls
