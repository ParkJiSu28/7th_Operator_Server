from rest_framework.viewsets import ModelViewSet
from .models import Group, Participate
from .serializers import GroupSerializer, MessageSerializer, ParticipateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action


# Create your views here.


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [SearchFilter]
    search_fields = ['GroupName']


class ParticipateViewSet(ModelViewSet):
    queryset = Participate.objects.all()
    serializer_class = ParticipateSerializer

    def get_queryset(self):
        qs = Participate.objects.all()
        member_id = self.request.query_params.get('member_id', None)
        if member_id is not None:
            member_id_qs = qs.filter(member_id=member_id)
            return member_id_qs

# 방 나가기 구현 삭제되면 GroupPid, schedule 같은 데이터 다 삭제
@api_view(['DELETE'])
def del_member(request, GroupPid, member_id):
    if request.method == 'DELETE':
        Participate.objects.filter(GroupPid=GroupPid,member_id=member_id).delete()
        message = Message(message="삭제 완료 되었습니다.")
        serializer = MessageSerializer(message)
        return Response(serializer.data)


#  그룹 닉네임 중복확인 함수 && 회원 여부 확인 && 비밀번호 확인
@api_view(['GET'])
def get_check_nick(request, GroupPid, Nickname, member_id, GroupPassword):
    if request.method == 'GET':
        part = Participate.objects.filter(GroupPid=GroupPid)
        part_nick = part.filter(Nickname=Nickname)
        part_member = Participate.objects.filter(GroupPid=GroupPid)
        pass_check = Group.objects.filter(GroupPassword=GroupPassword)
        if pass_check:
            if part_nick and part:
                message = Message(message="닉네임을 사용할 수 없습니다.")
                serializer = MessageSerializer(message)
                return Response(serializer.data)
            else:
                if part_member.filter(member_id=member_id):
                    message = Message(message="이미 참여하셨습니다.")
                    serializer = MessageSerializer(message)
                    return Response(serializer.data)
                else:
                    message = Message(message="닉네임을 사용할 수 있습니다.")
                    serializer = MessageSerializer(message)
                    return Response(serializer.data)
        else:
            message = Message(message="비밀번호가 일치하지 않습니다.")
            serializer = MessageSerializer(message)
            return Response(serializer.data)


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
