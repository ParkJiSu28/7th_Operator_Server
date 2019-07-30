from rest_framework.viewsets import ModelViewSet
from .models import Group
from .serializers import GroupSerializer, MessageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


#  가게이름 중복확인 함수
@api_view(['GET'])
def get_check(request, pk):
    if request.method == 'GET':
        if Group.objects.filter(GroupName=pk):
            message = Message(message="가게이름을 사용할 수 없습니다.")
            serializer = MessageSerializer(message)
            return Response(serializer.data)
        else:
            message = Message(message="가게이름으로 사용할 수 있습니다.")
            serializer = MessageSerializer(message)
            return Response(serializer.data)


# 메세지 통일을 위한 클래스.
class Message(object):
    def __init__(self, message, created=None):
        self.message = message
        self.created = created
