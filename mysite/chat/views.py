from django.shortcuts import render
from rest_framework import generics, mixins
from chat.models import ChatSpace, Message
from chat.serializers import ChatSpaceSerializer, MessageSerializer, ChatSpaceRetrivSerializer


# Create your views here.


class ChatSpaceList(generics.ListAPIView):
    queryset = ChatSpace.objects.all()
    serializer_class = ChatSpaceSerializer


class ChatSpaceDetail(generics.RetrieveAPIView):
    queryset = ChatSpace.objects.all()
    serializer_class = ChatSpaceRetrivSerializer


class CreateChatSpaceView(generics.CreateAPIView):
    serializer_class = ChatSpaceSerializer

    def perform_create(self, serializer):
        chat_name = serializer.validated_data['chat_name']

        if chat_name == "":
            chat_name = "Private conversation"
        serializer.save(chat_name=chat_name)


class RetrieveChatSpaceView(generics.RetrieveAPIView):
    pass


class CreateUpdateGetMessageView(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
