from rest_framework.viewsets import ModelViewSet
from .models import Schedule
from .serializers import ScheduleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter


class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
