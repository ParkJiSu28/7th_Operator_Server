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
    Nickname = models.ForeignKey('group.Participate', on_delete=models.CASCADE)
    SubstituteTF = models.BooleanField(default=False)


class Substitute(models.Model):
    SubstitutePid = models.AutoField(primary_key=True, blank=False)
    Requestor = models.CharField(blank=False,max_length=100)
    Responsor = models.CharField(null=True, blank=True,max_length=100)
    GroupPid = models.ForeignKey('Group', on_delete=models.CASCADE)
    SchedulePid = models.ForeignKey('schedule.Schedule', on_delete=models.CASCADE)
