from django.db import models


# Create your models here.
class Group(models.Model):
    GroupPid = models.AutoField(primary_key=True, blank=False)
    GroupName = models.CharField(unique=True, max_length=100)
    GroupPassword = models.CharField(blank=False,max_length=100)


class Substitute(models.Model):
    SubstitutePid = models.AutoField(primary_key=True, blank=False)
    Requestor = models.CharField(blank=False,max_length=100)
    Responsor = models.CharField(null=True, blank=True,max_length=100)
    GroupPid = models.ForeignKey('Group', on_delete=models.CASCADE)
    SchedulePid = models.ForeignKey('schedule.Schedule', on_delete=models.CASCADE)


class Participate(models.Model):
    member_id = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    GroupPid = models.ForeignKey('Group', on_delete=models.CASCADE)
    Nickname = models.CharField(primary_key=True, blank=False, max_length=100)
