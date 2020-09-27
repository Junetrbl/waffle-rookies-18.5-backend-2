from django.contrib.auth.models import User
from django.db import models


class ParticipantProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    university = models.CharField(max_length = 255, blank = True)
    accepted = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class InstructorProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    company = models.CharField(max_length = 255, blank = True)
    year = models.PositiveSmallIntegerField(null =True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Auth(models.Model):
    ROLE = (
        ('participant', 'participant'),
        ('instructor', 'instructor'),
    )
    user = models.ManyToManyField(
        User,
        on_delete = models.CASCADE,
        related_name = 'auths',
    )
    role = models.CharField(choices = ROLE)
