from django.db import models


class Schedule(models.Model):
    SchedulePid = models.AutoField(primary_key=True)
    GroupPid = models.ForeignKey('group.Group', on_delete=models.CASCADE)
    member_id = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    Date = models.DateField()
    StartHour = models.IntegerField(blank=False)
    StartMinute = models.IntegerField(blank=False)
    EndHour = models.IntegerField(blank=False)
    EndMinute = models.IntegerField(blank=False)
    Nickname = models.ForeignKey('group.Participate', on_delete=models.DO_NOTHING)
    SubstituteTF = models.BooleanField(default=False)


class Substitute(models.Model):
    SubstitutePid = models.AutoField(primary_key=True, blank=False)
    Requestor = models.ForeignKey('group.Participate',on_delete=models.DO_NOTHING,related_name='substitute_req')
    Responsor = models.ForeignKey('group.Participate',on_delete=models.DO_NOTHING,null=True,related_name='substitute_res')
    GroupPid = models.ForeignKey('group.Group', on_delete=models.CASCADE)
    SchedulePid = models.ForeignKey('Schedule', on_delete=models.CASCADE)
