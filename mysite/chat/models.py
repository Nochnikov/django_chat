from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class ChatSpace(models.Model):
    chat_name = models.CharField()
    is_private = models.BooleanField(default=True)
    is_super_group = models.BooleanField(default=False)


class Profile(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)
    has_avatar = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='message')
    chat_id = models.ForeignKey(ChatSpace, on_delete=models.CASCADE, related_name='chat')
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

    subscriptions = models.ManyToManyField(get_user_model())
