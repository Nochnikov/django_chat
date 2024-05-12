from django.urls import path
from authorization.views import RegistrationView, ChangePasswordView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registr/', RegistrationView.as_view(), name='registration'),
    path('reset-password/', ChangePasswordView.as_view(), name='reset_password')
]
