from django.urls import path
from chat.views import CreateChatSpaceView, ChatSpaceList

urlpatterns = [
    path('new_chat/', CreateChatSpaceView.as_view(), name='chat'),
    path('chat_space/', ChatSpaceList.as_view(), name='chat_space')
]