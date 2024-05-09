from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

# class ChatSpace(models.Model):
#     PRIVATE, PUBLIC = 1, 2
#
#     CHAT_TYPE = (
#         (PRIVATE, 'Private'),
#         (PUBLIC, 'Group'),
#     )
#     chat_name = models.CharField(null=True, blank=True, max_length=50)
#     created_at = models.DateTimeField(auto_now=True)
#     chat_type = models.CharField(choices=CHAT_TYPE, null=False)
#
#     users = models.ManyToManyField(get_user_model(), related_name='chat_spaces')
#
#     def __str__(self):
#         return f"{self.chat_name}, chat type: {self.chat_type}, super group: {self.is_super_group}"

class PrivateChat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(get_user_model(), related_name='private_chats')

    class Meta:
        db_table = 'chat_private_chat'


class PublicChat(models.Model):
    chat_name = models.CharField(max_length=50)
    chat_description = models.TextField(null=True, blank=True)
    owner = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(get_user_model(), related_name='public_chats')

    class Meta:
        db_table = 'chat_public_chat'


class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)
    avatar = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='message')
    private_chat = models.ForeignKey(PrivateChat, on_delete=models.CASCADE, related_name='messages', null=True)
    public_chat = models.ForeignKey(PublicChat, on_delete=models.CASCADE, related_name='messages', null=True)
    message_text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_updated(self):
        return self.sent_at != self.updated_at


class Group(models.Model):
    group_name = models.CharField(max_length=50, null=False)
    group_description = models.CharField(null=True)
    owner = models.CharField(max_length=50)

    users = models.ManyToManyField(get_user_model())
