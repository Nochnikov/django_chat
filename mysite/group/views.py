from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import views
from group.filters import GroupFilter
from group.models import Group
from group.serializers import GroupSerializer


# Create your views here.
class CreateGroupView(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'pk'

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GroupsListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    filterset_class = GroupFilter

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'pk'


class GroupsDetailView(generics.RetrieveUpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get_queryset(self):
        group = self.kwargs.get('pk')
        qs = Group.objects.all().filter(pk=group)
        return qs


class FollowGroupView(views.APIView):
    queryset = Group.objects.all()
    lookup_field = 'pk'

    def post(self, request, *args, **kwargs):
        group_id = kwargs.get('pk')
        request.user.group_set.add(group_id)
        return Response({'success followed': 'True'})


class UnfollowGroupView(views.APIView):
    queryset = Group.objects.all()
    lookup_field = 'pk'

    http_method_names = ['delete']

    def delete(self, request, *args, **kwargs):
        group_id = kwargs.get('pk')
        request.user.group_set.remove(group_id)
        return Response({'success unfollowed': 'True'})
