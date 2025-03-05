from django.urls import path
from .views import (
    RegisterView,
    UserDetailView,
    TestAuthView,
    LoginView,
    LogoutView
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='token_obtain'),
    path('logout/', LogoutView.as_view(), name='token_logout'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('test-auth/', TestAuthView.as_view(), name='test_auth'),
]