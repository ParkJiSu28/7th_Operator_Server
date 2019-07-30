from .models import Member
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class MessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)
