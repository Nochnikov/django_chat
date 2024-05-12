from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class DjangoModelPermissionsWithRead(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class DjangoObjectPermissionsWithReadUpdate(permissions.DjangoObjectPermissions):
    def has_object_permission(self, request, view, obj):
        user = request.user.username

        if request.method in permissions.SAFE_METHODS:
            return True

        return user == obj.owner


class IsChatMember(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):

        user = request.user

        if user in obj.private_chat.users.all():
            return True
        elif user in obj.public_chat.users.all():
            return True
        else:
            return False
