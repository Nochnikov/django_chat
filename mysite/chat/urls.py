from django.urls import path
from chat.views import CreateChatSpaceView, ChatSpaceList, CreateUpdateGetDeleteMessageView, ChatSpaceDetail, \
    CreateProfileView, RetrieveProfileView, GroupsListView, CreateGroupView, GroupsDetailView

urlpatterns = [
    path('new_chat/', CreateChatSpaceView.as_view(), name='chat'),
    path('chat_space/', ChatSpaceList.as_view(), name='chat_space'),
    path('chat_space/<int:pk>/', ChatSpaceDetail.as_view(), name='chat_info'),
    path('chat_space/<int:chat_id>/<int:pk>/', CreateUpdateGetDeleteMessageView.as_view(), name='messages'),
    path('profile/<int:user_id>/', RetrieveProfileView.as_view(), name='profile'),
    path('profile/update/<int:user_id>/', CreateProfileView.as_view(), name='edit_profile'),
    path('groups/create/', CreateGroupView.as_view(), name='create_group'),
    path('groups/', GroupsListView.as_view(), name='list_group'),
    path('groups/<int:pk>/', GroupsDetailView.as_view(), name='group_info')
]