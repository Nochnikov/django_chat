from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length=50, null=False)
    group_description = models.CharField(null=True)
    owner = models.CharField(max_length=50)

    users = models.ManyToManyField(get_user_model())

