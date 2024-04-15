from django.shortcuts import render
from rest_framework import generics
from chat.models import ChatSpace
from chat.serializers import ChatSpaceSerializer
from chat.models import Message

# Create your views here.


class ChatSpaceList(generics.ListAPIView):
    queryset = ChatSpace.objects.all()
    serializer_class = ChatSpaceSerializer


class CreateChatSpaceView(generics.CreateAPIView):
    serializer_class = ChatSpaceSerializer

    def perform_create(self, serializer):
        chat_name = serializer.validated_data['chat_name']

        if chat_name == "":
            chat_name = "Private conversation"
        serializer.save(chat_name=chat_name)



