from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import generics, status

from authorization.models import User
from authorization.serializers import LoginSerializer, RegisterSerializer, ChangePasswordSerializer


# Create your views here.


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)


class LogoutView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def get(self, request):
        logout(request)
        return Response({"detail": "Successfully logged out"})


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer

    def patch(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().patch(request, *args, **kwargs)

    def get_object(self):
        return self.request.user

