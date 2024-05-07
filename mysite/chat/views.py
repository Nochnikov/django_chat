import rest_framework.views
from django.shortcuts import render
from rest_framework import generics, mixins, permissions, status
from rest_framework.response import Response

from chat.filters import GroupFilter, MessageFilter
from chat.models import Message, Profile, Group, PrivateChat, PublicChat
from chat.serializers import MessageSerializer, ProfileSerializer, \
    ProfileDetailSerializer, GroupSerializer, PrivateChatSerializer, PublicChatSerializer
from django_filters import rest_framework as filters


# Create your views here.


# class ChatSpaceList(generics.ListAPIView):
#     queryset = ChatSpace.objects.all()
#     serializer_class = ChatSpaceSerializer
#
#     filter_class = ChatSpaceFilter
#
#     def get_queryset(self):
#         qs = ChatSpace.objects.all().filter(users=self.request.user)
#         return qs
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class ChatSpaceDetail(generics.RetrieveAPIView):
#     queryset = ChatSpace.objects.all()
#     serializer_class = ChatSpaceRetrivSerializer
#     lookup_field = 'pk'


# class CreateChatSpaceView(generics.CreateAPIView):
#     serializer_class = ChatSpaceSerializer
#
#     def perform_create(self, serializer):
#         chat_name = serializer.validated_data['chat_name']
#
#         if chat_name == "":
#             chat_name = "Private conversation"
#
#         serializer.save(chat_name=chat_name, user=self.request.user)

class DeleteUpdatePublicChatView(generics.GenericAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    queryset = PublicChat.objects.all()
    serializer_class = PublicChatSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ListCreatePublicChat(generics.ListCreateAPIView):
    queryset = PublicChat.objects.all()
    serializer_class = PublicChatSerializer

    def get_queryset(self):
        qs = PublicChat.objects.all().filter(users=self.request.user.pk)
        return qs

    def perform_create(self, serializer):
        user = self.request.user
        users = serializer.validated_data.get("users")

        if user in users:
            users.remove(user)
        users.append(user)

        serializer.save(owner=self.request.user)


class DeletePrivateChatView(generics.DestroyAPIView):
    queryset = PrivateChat.objects.all()
    serializer_class = PrivateChatSerializer


class ListCreatePrivateChat(generics.ListCreateAPIView):
    queryset = PrivateChat.objects.all()
    serializer_class = PrivateChatSerializer

    def get_queryset(self):
        qs = PrivateChat.objects.all().filter(users=self.request.user)
        return qs

    def perform_create(self, serializer):
        user = self.request.user
        users = serializer.validated_data.get('users')

        if user in users:
            users.remove(user)
        users.append(user)

        if len(users) != 2:
            return Response({'error': 'Private chat must contain exactly 2 users'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()


class ChatListView(generics.ListAPIView):
    queryset = PrivateChat.objects.all()
    serializer_class = PrivateChatSerializer

    def get_queryset(self):
        user = self.request.user
        private_chats = PrivateChat.objects.filter(users=user)
        public_chats = PublicChat.objects.filter(users=user)

        qs = list(private_chats) + list(public_chats)

        return qs

    def perform_create(self, serializer):
        serializer.save(users=self.request.user)


class CreateUpdateGetDeleteMessageView(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    filter_class = MessageFilter

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateProfileView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(self, request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user_id)


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
