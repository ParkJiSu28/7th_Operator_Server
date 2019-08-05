from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, get_check, ParticipateViewSet, ParticipatedGroupViewSet, create_group, get_check_nick, del_member

# 방 검색
router = DefaultRouter()
router.register('', GroupViewSet)

# 방 참여
part = ParticipateViewSet.as_view({'post': 'create'})

# 참여중인 방 조회
part_list = ParticipatedGroupViewSet.as_view({'get': 'list'})


part_detail = ParticipateViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


urlpatterns = [
    path('', include(router.urls)),
    path('namecheck/<str:pk>', get_check),
    path('create', create_group),
    path('signed', part_list),
    path('sign', part),
    path('sign/<int:pk>', part_detail),
    path('check/<int:GroupPid>/<str:Nickname>/<str:member_id>/<str:GroupPassword>', get_check_nick),
    path('delete/<int:GroupPid>/<str:member_id>', del_member),

]
