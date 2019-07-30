from .models import Group
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class MessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)
