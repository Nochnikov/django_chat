from django_filters import rest_framework as filters

from chat.models import Message


def value_contains(queryset, name, value):
    look_up = f"{name}__icontains"
    return queryset.filter(**{look_up: value})


class MessageFilter(filters.FilterSet):
    message_text = filters.CharFilter(field_name='message_text', method=value_contains)

    class Meta:
        model = Message
        fields = {'message_text': ['exact', 'icontains']}
