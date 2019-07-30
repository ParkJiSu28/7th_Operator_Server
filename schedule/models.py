from django.db import models


class Schedule(models.Model):
    SchedulePid = models.AutoField(primary_key=True)
    GroupPid = models.ForeignKey('group.Group', on_delete=models.CASCADE)
    member_id = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    Date = models.CharField(max_length=30)
    StartHour = models.IntegerField(blank=False)
    StartMinute = models.IntegerField(blank=False)
    EndHour = models.IntegerField(blank=False)
    EndMinute = models.IntegerField(blank=False)
