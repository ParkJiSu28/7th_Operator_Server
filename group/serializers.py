from .models import Group, Participate, Substitute
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
import sys

sys.path.append("..")
from member.serializers import MemberSerializer


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class ParticipateSerializer(ModelSerializer):
    GroupKey = GroupSerializer(read_only=True)
    MemberKey = MemberSerializer(read_only=True)

    class Meta:
        model = Participate
        fields = '__all__'


class MessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)
