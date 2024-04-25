from rest_framework import serializers

from authorization.models import User
from chat.models import ChatSpace, Message, Profile, Group


class ChatSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSpace
        fields = ['chat_name', 'chat_type']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('user', 'chat', 'message_text')


class ChatSpaceRetrivSerializer(serializers.ModelSerializer):
    # message = LastMessageSerializer(read_only=True)

    class Meta:
        model = ChatSpace
        fields = ("chat_name", "chat_type", 'created_at')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name')


class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'is_premium', 'is_active', 'is_stuff')


class GroupSerializer(serializers.ModelSerializer):

    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'group_name', 'group_description', "users")
