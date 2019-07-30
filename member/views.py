from rest_framework.viewsets import ModelViewSet
from .models import Member
from .serializers import MemberSerializer, MessageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# 아이디 회원 가입
# Create your views here.
class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


# 아디이 중복확인 함수
@api_view(['GET'])
def get_check(request, pk):
    if request.method == 'GET':
        if Member.objects.filter(member_id=pk):
            message = Message(message="아이디를 사용할 수 없습니다.")
            serializer = MessageSerializer(message)
            return Response(serializer.data)
        else:
            message = Message(message="아이디를 사용할 수 있습니다.")
            serializer = MessageSerializer(message)
            return Response(serializer.data)


# 메세지 통일을 위한 클래스.
class Message(object):
    def __init__(self, message, created=None):
        self.message = message
        self.created = created
