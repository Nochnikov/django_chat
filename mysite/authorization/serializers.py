from rest_framework import serializers

from authorization.models import User


class LoginSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = ('username', 'password')
