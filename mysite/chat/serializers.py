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


class LastMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = 'last_message'


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


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('group_name', 'group_description', 'users')
