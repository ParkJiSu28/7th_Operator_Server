from .models import Schedule,Substitute
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
import sys

sys.path.append("..")
from group.serializers import ParticipateSerializer,GroupSerializer
from member.serializers import MemberSerializer


class ScheduleSerializer(ModelSerializer):
    GroupKey = GroupSerializer(read_only=True)
    ParticipateKey = ParticipateSerializer(read_only=True)
    MemberKey = MemberSerializer(read_only=True)

    class Meta:
        model = Schedule
        fields = '__all__'

class SubstituteSerializer(ModelSerializer):
    ScheduleKey = ScheduleSerializer(read_only=True)
    GroupKey = GroupSerializer(read_only=True)

    class Meta:
        model = Substitute
        fields = '__all__'


class MessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)
