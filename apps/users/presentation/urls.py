from django.urls import path
from .views import UserListCreateView, UserDetailView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('<str:user_id>/', UserDetailView.as_view(), name='user-detail'),
]
