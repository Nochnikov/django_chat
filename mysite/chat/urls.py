from django.urls import path
from chat.views import CreateChatSpaceView, ChatSpaceList, CreateUpdateGetDeleteMessageView, ChatSpaceDetail, \
    CreateProfileView

urlpatterns = [
    path('new_chat/', CreateChatSpaceView.as_view(), name='chat'),
    path('chat_space/', ChatSpaceList.as_view(), name='chat_space'),
    path('chat/<int:pk>', ChatSpaceDetail.as_view(), name='chat_info'),
    path('chat_space/<int:chat_id>/<int:pk>', CreateUpdateGetDeleteMessageView.as_view(), name='messages'),
    path('profile/', CreateProfileView.as_view(), name='edit_profile')
]