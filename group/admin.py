from django.contrib import admin
from .models import Group, Participate


@admin.register(Group)
@admin.register(Participate)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['GroupPid',]


class ParticipateAdmin(admin.ModelAdmin):
    list_display = ['Nickname',]
