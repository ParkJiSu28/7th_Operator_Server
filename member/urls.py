from django.urls import path, include
from .views import MemberViewSet,get_check
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register', MemberViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('idcheck/<str:pk>', get_check),

]
