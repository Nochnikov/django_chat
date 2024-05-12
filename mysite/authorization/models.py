from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from authorization.managers import UserManager


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    ADMIN, MODER, USER = 1, 2, 3
    ROLES = (
        (ADMIN, 'admin'),
        (MODER, 'moderator'),
        (USER, 'user'),
    )

    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(choices=ROLES, default=USER)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

