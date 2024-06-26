import rest_framework.views
from rest_framework import generics, mixins, permissions
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.response import Response
from chat.permissions import DjangoModelPermissionsWithRead, IsChatMember, DjangoObjectPermissionsWithReadUpdate
from chat.filters import GroupFilter, MessageFilter
from chat.models import Message, Profile, Group, PrivateChat, PublicChat
from chat.serializers import PrivateMessageSerializer, ProfileSerializer, \
    ProfileDetailSerializer, GroupSerializer, PrivateChatSerializer, PublicChatSerializer, PublicMessageSerializer, \
    ChatSerializer


# Create your views here.

class DeleteUpdatePublicChatView(generics.GenericAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    queryset = PublicChat.objects.all()
    serializer_class = PublicChatSerializer

    permission_classes = [permissions.DjangoModelPermissions]

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ListCreatePublicChat(generics.ListCreateAPIView):
    queryset = PublicChat.objects.all()
    serializer_class = PublicChatSerializer

    permission_classes = [permissions.DjangoModelPermissions]

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
    permission_classes = [permissions.DjangoModelPermissions]


class ListCreatePrivateChat(generics.ListCreateAPIView):
    queryset = PrivateChat.objects.all()
    serializer_class = PrivateChatSerializer

    permission_classes = [permissions.DjangoModelPermissions]

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
            raise ValidationError("Chat have to contain exactly two users")

        serializer.save()


class ChatListView(generics.ListAPIView):
    queryset = PrivateChat.objects.all()
    serializer_class = ChatSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        private_chats = PrivateChat.objects.filter(users=user)
        public_chats = PublicChat.objects.filter(users=user)

        qs = list(private_chats) + list(public_chats)

        return qs


class CreateUpdateGetDeletePublicMessageView(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin):
    queryset = Message.objects.all()
    serializer_class = PublicMessageSerializer
    lookup_field = 'pk'
    filterset_class = MessageFilter

    permission_classes = [IsChatMember]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_queryset(self):
        chat_id = self.kwargs.get('public_chat_id')

        qs = Message.objects.filter(public_chat_id=chat_id).all()

        public_chat = PublicChat.objects.get(pk=chat_id)

        user = self.request.user

        if user not in public_chat.users.all():
            raise PermissionDenied("You do not have permission to perform this action")
        return qs

    def perform_create(self, serializer):
        public_chat = self.kwargs.get('public_chat_id')

        serializer.save(user=self.request.user, public_chat_id=public_chat)


class CreateUpdateGetDeletePrivateMessageView(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin):
    queryset = Message.objects.all()
    serializer_class = PrivateMessageSerializer
    lookup_field = 'pk'
    filterset_class = MessageFilter

    permission_classes = [IsChatMember]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_queryset(self):
        chat_id = self.kwargs.get('private_chat_id')

        user = self.request.user

        qs = Message.objects.filter(private_chat_id=chat_id).all()

        private_chat = PrivateChat.objects.get(pk=chat_id)

        if user not in private_chat.users.all():
            raise PermissionDenied("You do not have permission to perform this action.")

        return qs

    def perform_create(self, serializer):
        private_chat = self.kwargs.get('private_chat_id')

        serializer.save(user=self.request.user, private_chat_id=private_chat)


class CurrentUserProfileView(generics.GenericAPIView,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.RetrieveModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    permission_classes = [permissions.DjangoModelPermissions]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_object(self):
        instance = Profile.objects.get(user=self.request.user)
        return instance


class RetrieveProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    lookup_field = 'user_id'

    permissions_classes = [permissions.DjangoModelPermissions]


class CreateGroupView(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'pk'

    permission_classes = [permissions.DjangoModelPermissions]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GroupsListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    filterset_class = GroupFilter

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'pk'

    permission_classes = [DjangoModelPermissionsWithRead]


class GroupsDetailView(generics.RetrieveUpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'pk'
    permission_classes = [DjangoObjectPermissionsWithReadUpdate]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get_queryset(self):
        group = self.kwargs.get('pk')
        qs = Group.objects.all().filter(pk=group)
        return qs


class FollowGroupView(rest_framework.views.APIView):
    queryset = Group.objects.all()
    lookup_field = 'pk'

    def post(self, request, *args, **kwargs):
        group_id = kwargs.get('pk')
        request.user.group_set.add(group_id)
        return Response({'success followed': 'True'})


class UnfollowGroupView(rest_framework.views.APIView):
    queryset = Group.objects.all()
    lookup_field = 'pk'

    permission_classes = [permissions.DjangoModelPermissions]

    http_method_names = ['delete']

    def delete(self, request, *args, **kwargs):
        group_id = kwargs.get('pk')
        request.user.group_set.remove(group_id)
        return Response({'success unfollowed': 'True'})
