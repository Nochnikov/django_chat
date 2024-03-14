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


class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)
    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)
    has_avatar = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_id = models.ForeignKey(ChatSpace, on_delete=models.CASCADE)
    message = models.TextField()

