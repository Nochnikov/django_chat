from django.urls import path
from chat.views import CreateChatSpaceView, ChatSpaceList, CreateUpdateGetDeleteMessageView, ChatSpaceDetail, \
    CreateProfileView, RetrieveProfileView, GroupsView

urlpatterns = [
    path('new_chat/', CreateChatSpaceView.as_view(), name='chat'),
    path('chat_space/', ChatSpaceList.as_view(), name='chat_space'),
    path('chat_space/<int:pk>/', ChatSpaceDetail.as_view(), name='chat_info'),
    path('chat_space/<int:chat_id>/<int:pk>/', CreateUpdateGetDeleteMessageView.as_view(), name='messages'),
    path('profile/<int:user_id>/', RetrieveProfileView.as_view(), name='profile'),
    path('profile/update/<int:user_id>/', CreateProfileView.as_view(), name='edit_profile'),
    path('profile/<int:user_id>/groups/', GroupsView.as_view(), name='groups')
]