from django_filters import rest_framework as filters

from chat.models import Group, Message


class GroupFilter(filters.FilterSet):
    users = filters.CharFilter('users__username', lookup_expr='icontains')

    class Meta:
        model = Group
        fields = {'users': ['exact', 'icontains']}


class MessageFilter(filters.FilterSet):

    id = filters.CharFilter('message__user_id', lookup_expr='exact')

