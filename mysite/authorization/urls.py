from django.contrib.auth.views import PasswordResetView
from django.urls import path
from authorization.views import LogoutView, RegistrationView, ChangePasswordView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registr/', RegistrationView.as_view(), name='registration'),
    path('reset-password/', ChangePasswordView.as_view(), name='reset_password')
]
