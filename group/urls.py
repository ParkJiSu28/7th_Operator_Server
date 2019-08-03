from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, get_check, ParticipateViewSet, get_check_nick, del_member

router = DefaultRouter()
router.register('', GroupViewSet)
part_list = ParticipateViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
part_detail = ParticipateViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('', include(router.urls)),
    path('namecheck/<str:pk>', get_check),
    path('sign', part_list),
    path('sign/<int:pk>', part_detail),
    path('check/<int:GroupPid>/<str:Nickname>/<str:member_id>/<str:GroupPassword>', get_check_nick),
    path('delete/<int:GroupPid>/<str:member_id>', del_member),

]
