import rest_framework.views
from django.shortcuts import render
from rest_framework import generics, mixins, permissions
from rest_framework.response import Response

from chat.filters import GroupFilter
from chat.models import ChatSpace, Message, Profile, Group
from chat.serializers import ChatSpaceSerializer, MessageSerializer, ChatSpaceRetrivSerializer, ProfileSerializer, \
    ProfileDetailSerializer, GroupSerializer
from django_filters import rest_framework as filters


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


class CreateGroupView(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'pk'


class GroupsListView(generics.ListAPIView):
    filterset_class = GroupFilter

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'pk'


class GroupsDetailView(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'pk'


class JoinGroupView(rest_framework.views.APIView):
    queryset = Group.objects.all()
    lookup_field = 'pk'

    permission_classes = [permissions.DjangoModelPermissions]

    def post(self, request, *args, **kwargs):
        group_id = kwargs.get('pk')
        request.user.group_set.add(group_id)
        return Response({'success joint': 'True'})
