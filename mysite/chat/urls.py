from django.urls import path
from chat.views import (RetrieveProfileView, GroupsListView, CreateGroupView, GroupsDetailView,
                        JoinGroupView, ChatListView, ListCreatePrivateChat, ListCreatePublicChat,
                        DeleteUpdatePublicChatView,
                        DeletePrivateChatView, CreateUpdateGetDeletePrivateMessageView,
                        CreateUpdateGetDeletePublicMessageView, CurrentUserProfileView, )
urlpatterns = [
    path('', ChatListView.as_view(), name='chat-list'),
    path('private/', ListCreatePrivateChat.as_view(), name='chat-private'),
    path('private/<int:pk>/', DeletePrivateChatView.as_view(), name='chat-private-delete'),
    path('private/<int:private_chat_id>/messages/', CreateUpdateGetDeletePrivateMessageView.as_view(), name='chat-private-messages'),
    path('private/<int:private_chat_id>/messages/<int:pk>/', CreateUpdateGetDeletePrivateMessageView.as_view(), name='chat-private-messages-delete-update'),

    path('public/', ListCreatePublicChat.as_view(), name='chat-public'),
    path('public/<int:pk>/', DeleteUpdatePublicChatView.as_view(), name='chat-public-delete'),
    path('public/<int:public_chat_id>/messages/', CreateUpdateGetDeletePublicMessageView.as_view(), name='chat-public-messages' ),
    path('public/<int:public_chat_id>/messages/<int:pk>/', CreateUpdateGetDeletePublicMessageView.as_view(), name='chat-public-messages-delete-update' ),


    path('profile/me/', CurrentUserProfileView.as_view(), name='profile'),
    path('profile/<int:user_id>/', RetrieveProfileView.as_view(), name='profile_others'),

    path('groups/create/', CreateGroupView.as_view(), name='create_group'),
    path('groups/', GroupsListView.as_view(), name='list_group'),
    path('groups/<int:pk>/', GroupsDetailView.as_view(), name='group_info'),
    path('groups/<int:pk>/join/', JoinGroupView.as_view(), name='group_join'),

]

