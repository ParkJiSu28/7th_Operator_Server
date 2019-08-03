from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScheduleViewSet,get_month_pk,post_schedule,SubstituteViewSet

sche_list = ScheduleViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
sche_detail = ScheduleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

sub_list = SubstituteViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
sub_detail = SubstituteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


urlpatterns = [
    path('', sche_list),
    path('<int:pk>',sche_detail),
    path("daily/<int:SchedulePid>",get_month_pk),
    path('post',post_schedule),
    path('cover',sub_list),
    path('cover/<int:pk>',sub_detail),
]