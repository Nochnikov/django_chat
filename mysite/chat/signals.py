
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from chat.models import Profile


@receiver(post_save, sender=get_user_model())
def create_profile(created, **kwargs):
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)
        print(f'Profile for {instance} created!')


@receiver(post_delete, sender=Profile)
def delete_user(instance, **kwargs):
    user = instance.user
    user.delete()