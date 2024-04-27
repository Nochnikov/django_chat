from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class ChatSpace(models.Model):
    PRIVATE, PUBLIC = 1, 2

    CHAT_TYPE = (
        (PRIVATE, 'Private'),
        (PUBLIC, 'Group'),
    )
    chat_name = models.CharField(null=True, blank=True, max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    chat_type = models.CharField(choices=CHAT_TYPE, null=False)
    is_super_group = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.chat_name}, chat type: {self.chat_type}, super group: {self.is_super_group}"


class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)
    has_avatar = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='message')
    chat = models.ForeignKey(ChatSpace, on_delete=models.CASCADE, related_name='chat')
    message_text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type_is = models.CharField(max_length=50)

    @property
    def is_updated(self):
        return self.sent_at != self.updated_at



class Group(models.Model):
    group_name = models.CharField(max_length=50, null=False)
    group_description = models.CharField(null=True)

    users = models.ManyToManyField(get_user_model())
