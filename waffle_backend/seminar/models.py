from django.db import models
from django.contrib.auth.models import User


class Seminar(models.Model):
    name = models.CharField(max_length = 200)
    capacity = models.PositiveSmallIntegerField()
    count = models.PositiveSmallIntegerField()
    time = models.TimeField()
    online = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class UserSeminar(models.Model):
    role_list = (
        ('participant', 'participant'),
        ('instructor', 'instructor'),
    )


    user = models.ForeignKey(User, on_delete = models.CASCADE)
    seminar = models.ForeignKey(Seminar, on_delete = models.CASCADE)
    role = models.CharField(choices=role_list, blank = True, max_length = 100, db_index=True)
    is_active = models.BooleanField(default = True)
    dropped_at = models.DateTimeField(auto_now_add=False, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'seminar'], name='userseminar_unique')
        ]