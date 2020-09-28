from django.contrib.auth.models import User
from django.db import models


class ParticipantProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name = 'participant',
        on_delete=models.CASCADE,
    )
    university = models.CharField(max_length = 255, blank = True, default = "")
    accepted = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class InstructorProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name = 'instructor',
        on_delete=models.CASCADE,
    )
    company = models.CharField(max_length = 255, blank = True, default = "")
    year = models.SmallIntegerField(null =True, default = None)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class UserAuth(models.Model):
    user = models.OneToOneField(User, related_name = 'auth', on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
