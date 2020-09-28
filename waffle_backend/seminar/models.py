from django.db import models
from django.contrib.auth.models import User


class Seminar(models.Model):
    name = models.CharField(max_length = 200)
    capacity = models.IntegerField
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class UserSeminar(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    seminar = models.ForeignKey(Seminar, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)