from .models import Schedule
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
import sys

sys.path.append("..")
from member.serializers import MemberSerializer
from group.serializers import GroupSerializer, ParticipateSerializer


class ScheduleSerializer(ModelSerializer):
    GroupKey = GroupSerializer(read_only=True)
    MemberKey = MemberSerializer(read_only=True)
    ParticipateKey = ParticipateSerializer(read_only=True)

    class Meta:
        model = Schedule
        fields = '__all__'


class MessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)
