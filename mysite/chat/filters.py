from django_filters import rest_framework as filters

from chat.models import Group, Message


class GroupFilter(filters.FilterSet):
    users = filters.CharFilter('users__username', lookup_expr='icontains')

    class Meta:
        model = Group
        fields = {'users': ['exact', 'icontains']}


def message_contains(queryset, name, value):
    look_up = f"{name}__icontains"
    return queryset.filter(**{look_up: value})


class MessageFilter(filters.FilterSet):
    message_text = filters.CharFilter(field_name='message_text', method=message_contains)

    class Meta:
        model = Message
        fields = {'message_text': ['exact', 'icontains']}
