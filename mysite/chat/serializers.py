from rest_framework import serializers
from chat.models import ChatSpace


class ChatSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSpace
        fields = ['chat_name', 'chat_type']
