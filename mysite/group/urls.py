from django.urls import path

from group.views import GroupsListView, CreateGroupView, GroupsDetailView, FollowGroupView, UnfollowGroupView

urlpatterns = [
    path('', GroupsListView.as_view(), name='list_group'),
    path('create/', CreateGroupView.as_view(), name='create_group'),
    path('<int:pk>/', GroupsDetailView.as_view(), name='group_info'),
    path('<int:pk>/subscribe/', FollowGroupView.as_view(), name='group_join'),
    path('<int:pk>/unsubsribe/', UnfollowGroupView.as_view(), name='group_unjoin'),
]
