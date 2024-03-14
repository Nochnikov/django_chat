from django.db import models


# Create your models here.

class ChatSpace(models.Model):
    chat_name = models.CharField()
    is_private = models.BooleanField(default=True)
    is_super_group = models.BooleanField(default=False)


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=10)

    chat = models.ManyToManyField(ChatSpace)
    friends = models.ManyToManyField('User')


class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    is_premium = models.BooleanField(default=False)
    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)
    has_avatar = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message')
    chat_id = models.ForeignKey(ChatSpace, on_delete=models.CASCADE, related_name='chat')
    message_text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type_is = models.CharField(max_length=50)

    @property
    def is_updated(self):
        return self.sent_at != self.updated_at

