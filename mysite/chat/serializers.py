from rest_framework import serializers

from authorization.models import User
from chat.models import ChatSpace, Message, Profile, Group


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'is_premium', 'is_active')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ChatSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSpace
        fields = ['chat_name', 'chat_type', 'users']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('user', 'chat', 'message_text')


class ProfileDetailSerializer(serializers.ModelSerializer):
    user_info = UserProfileSerializer(read_only=True, source='user')

    class Meta:
        model = Profile
        fields = ('user_id', 'user_info', 'first_name', 'last_name', 'created_at')


class ChatSpaceRetrivSerializer(serializers.ModelSerializer):
    # message = LastMessageSerializer(read_only=True)
    class Meta:
        model = ChatSpace
        fields = ("chat_name", "chat_type", 'created_at', 'users')


class GroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'group_name', 'group_description', "users")
