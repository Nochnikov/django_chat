from rest_framework import serializers
from chat.models import ChatSpace, Message, Profile


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
