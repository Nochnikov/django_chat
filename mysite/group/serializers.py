from rest_framework import serializers

from authorization.models import User
from group.models import Group


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'is_premium', 'is_active')


class GroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'group_name', "owner", 'group_description', "users")
        read_only_fields = ['owner']
