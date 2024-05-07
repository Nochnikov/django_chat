from rest_framework import serializers

from authorization.models import User
from chat.models import Message, Profile, Group, PrivateChat, PublicChat


class PublicChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicChat
        fields = ['pk', 'chat_name', 'chat_description', 'users']


class PrivateChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateChat
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'is_premium', 'is_active')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PrivateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('user', 'private_chat', 'message_text')
        read_only_fields = ['user', 'private_chat']


class PublicMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('user', 'public_chat', 'message_text')
        read_only_fields = ['user', 'public_chat']


class ProfileDetailSerializer(serializers.ModelSerializer):
    user_info = UserProfileSerializer(read_only=True, source='user')

    class Meta:
        model = Profile
        fields = ('user_id', 'user_info', 'first_name', 'last_name', 'created_at')


class GroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'group_name', 'group_description', "users")
