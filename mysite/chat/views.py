from django.shortcuts import render
from rest_framework import generics, mixins
from chat.models import ChatSpace, Message, Profile, Group
from chat.serializers import ChatSpaceSerializer, MessageSerializer, ChatSpaceRetrivSerializer, ProfileSerializer, \
    ProfileDetailSerializer, GroupSerializer


# Create your views here.


class ChatSpaceList(generics.ListAPIView):
    queryset = ChatSpace.objects.all()
    serializer_class = ChatSpaceSerializer


class ChatSpaceDetail(generics.RetrieveAPIView):
    queryset = ChatSpace.objects.all()
    serializer_class = ChatSpaceRetrivSerializer
    lookup_field = 'pk'


class CreateChatSpaceView(generics.CreateAPIView):
    serializer_class = ChatSpaceSerializer

    def perform_create(self, serializer):
        chat_name = serializer.validated_data['chat_name']

        if chat_name == "":
            chat_name = "Private conversation"
        serializer.save(chat_name=chat_name)


class CreateUpdateGetDeleteMessageView(
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


class CreateProfileView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(self, request, *args, **kwargs)


class RetrieveProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    lookup_field = 'user_id'


class GroupsView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'pk'