from django.db import models
from django.contrib.auth.models import User


class Seminar(models.Model):
    name = models.CharField(max_length = 200, blank = True, unique = True)
    capacity = models.SmallIntegerField()
    count = models.SmallIntegerField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    online = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class UserSeminar(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    seminar = models.ForeignKey(Seminar, on_delete = models.CASCADE)
    role = models.CharField(max_length = 200, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)