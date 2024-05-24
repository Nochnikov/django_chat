from django_filters import rest_framework as filters

from group.models import Group


def value_contains(queryset, name, value):
    look_up = f"{name}__icontains"
    return queryset.filter(**{look_up: value})


class GroupFilter(filters.FilterSet):
    users = filters.CharFilter('users__username', lookup_expr='icontains')

    group_name = filters.CharFilter(field_name='group_name', method=value_contains)

    class Meta:
        model = Group
        fields = {'users': ['exact', 'icontains'],
                  'group_name': ['exact', 'icontains']}
