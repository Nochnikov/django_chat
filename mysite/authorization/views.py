from django.contrib.auth import login, authenticate, logout
from rest_framework.response import Response
from rest_framework import generics

from authorization.models import User
from authorization.serializers import LoginSerializer


# Create your views here.


class LoginView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return Response({"detail": "Successfully logged in!"})
        return Response({"detail": "Unsuccessful login"})


class LogoutView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def get(self, request):
        logout(request)
        return Response({"detail": "Successfully logged out"})
