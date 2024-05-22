from django.contrib.auth.hashers import make_password
from rest_framework import generics, permissions
from authorization.models import User
from authorization.serializers import RegisterSerializer, ChangePasswordSerializer


# Create your views here.


class RegistrationView(generics.CreateAPIView):

    permission_classes = [permissions.AllowAny]

    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer

    def patch(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().patch(request, *args, **kwargs)

    def get_object(self):
        return self.request.user
