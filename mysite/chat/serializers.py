from rest_framework import serializers
from chat.models import ChatSpace, Message


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
    message = LastMessageSerializer(read_only=True)

    class Meta:
        model = ChatSpace
        fields = ("chat_name", "chat_type", 'message', 'created_at')
