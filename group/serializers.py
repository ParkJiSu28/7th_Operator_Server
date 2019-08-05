from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Group, Participate
import sys
sys.path.append("..")
from member.serializers import MemberSerializer


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['GroupPid','GroupName']


class ParticipateSerializer(ModelSerializer):
    GroupKey = GroupSerializer(read_only=True)
    MemberKey = MemberSerializer(read_only=True)

    class Meta:
        model = Participate
        fields = '__all__'

# 참여중인 방 조회
class Participated_Group_Serializer(ModelSerializer):
    GroupPid = GroupSerializer(read_only=True)
    member_id = MemberSerializer(read_only=True)

    class Meta:
        model = Participate
        fields = ['member_id', 'GroupPid', 'Nickname']

class MessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)