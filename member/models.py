from django.db import models


# Create your models here.

class Member(models.Model):
    member_id = models.CharField(primary_key=True, unique=True, max_length=50)
