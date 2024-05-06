from django.urls import path
from chat.views import (CreateProfileView, RetrieveProfileView, GroupsListView, CreateGroupView, GroupsDetailView,
                        JoinGroupView, ChatListView, ListCreatePrivateChat, ListCreatePublicChat)

urlpatterns = [
    path('', ChatListView.as_view(), name='chat-list'),
    path('private/', ListCreatePrivateChat.as_view(), name='chat-private'),
    path('public/', ListCreatePublicChat.as_view(), name='chat-public'),
    path('profile/<int:user_id>/', RetrieveProfileView.as_view(), name='profile'),
    path('profile/update/<int:user_id>/', CreateProfileView.as_view(), name='edit_profile'),
    path('groups/create/', CreateGroupView.as_view(), name='create_group'),
    path('groups/', GroupsListView.as_view(), name='list_group'),
    path('groups/<int:pk>/', GroupsDetailView.as_view(), name='group_info'),
    path('groups/<int:pk>/join/', JoinGroupView.as_view(), name='group_join'),

]