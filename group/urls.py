from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, get_check

router = DefaultRouter()
router.register('', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('namecheck/<str:pk>', get_check),
]
