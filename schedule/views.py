from rest_framework.viewsets import ModelViewSet
from .models import Schedule, Substitute
from .serializers import ScheduleSerializer, MessageSerializer, SubstituteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import sys

sys.path.append("..")
from group.models import Participate


class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    # 달에 맞춰서 일정 보내주기
    def get_queryset(self):
        qs = super().get_queryset()
        gp = self.request.query_params.get('GroupPid')
        date = self.request.query_params.get('Date')
        sc_pr = qs.filter(GroupPid=gp)
        year = date[0:4]
        month = date[5:7]
        year_qs = sc_pr.filter(Date__year=year)
        month_qs = year_qs.filter(Date__month=month)
        return month_qs


# 세부일정 조회 삭제 수정
@api_view(['GET', 'DELETE', 'PUT'])
def get_month_pk(request, SchedulePid):
    if request.method == 'GET':

        if Schedule.objects.filter(SchedulePid=SchedulePid):
            Schedule_PK = Schedule.objects.get(SchedulePid=SchedulePid)
            serializer = ScheduleSerializer(Schedule_PK)
            return Response(serializer.data)
        else:
            message = Message(message="일정이 존재하지 않습니다.")
            serializer = MessageSerializer(message)
            return Response(serializer.data)

    if request.method == 'DELETE':
        Schedule.objects.filter(SchedulePid=SchedulePid).delete()
        message = Message(message="삭제 완료 되었습니다.")
        serializer = MessageSerializer(message)
        return Response(serializer.data)

    if request.method == 'PUT':
        Schedule_PK = Schedule.objects.get(SchedulePid=SchedulePid)
        serializer = ScheduleSerializer(Schedule_PK)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


# 일정 추가 & 모든 일정 조회
@api_view(['GET', 'POST'])
def post_schedule(request):
    if request.method == 'POST':
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == 'GET':
        queryset = Schedule.objects.all()
        serializer = ScheduleSerializer(queryset, many=True)
        return Response(serializer.data)


class SubstituteViewSet(ModelViewSet):
    queryset = Substitute.objects.all()
    serializer_class = SubstituteSerializer

    # SchedulePid로 일정 조회해서 SubstituteTF True로 만들어주기
    def perform_create(self, serializer):
        sche_pr = self.request.data['SchedulePid']
        subTF = Schedule.objects.get(SchedulePid=sche_pr)
        subTF.SubstituteTF = True
        subTF.save()
        serializer.save()

    # SchedulePid로 일정 조회해서 닉네임과 아이디 그리고 SubstituteTF False만들기
    #foregin key 어떻게 해야하냐 아..개짱난다..
    def perform_update(self, serializer):
        sche_pr = self.request.data['SchedulePid']
        subTF = Schedule.objects.get(SchedulePid=sche_pr)
        Res = self.request.data['Responsor']
        subTF.SubstituteTF = False
        grpid = subTF.GroupPid
        nick = Participate.objects.get(Nickname=Res, GroupPid=grpid)
        subTF.Nickname = nick.Nick
        req = self.request.data['Requestor']
        mem_id = Participate.objects.get(Nickname=req, GroupPid=grpid)
        subTF.member_id = mem_id.member_id
        serializer.save()


# 메세지 통일을 위한 클래스.
class Message(object):
    def __init__(self, message, created=None):
        self.message = message
        self.created = created
