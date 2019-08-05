from django.contrib import admin
from .models import Schedule, Substitute


# Register your models here.

@admin.register(Schedule)
@admin.register(Substitute)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['SchedulePid',]


class SubstituteAdmin(admin.ModelAdmin):
    list_display = ['SubstitutePid','GroupPid']
