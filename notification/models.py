from users.models import User
from django.db import models

# Create your models here.


class Activity(models.IntegerChoices):
    Exercise = 1


class ActivityMessageMaster(models.Model):
    activity = models.PositiveIntegerField(choices=Activity.choices, default=Activity.Exercise)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.SmallIntegerField()
    message = models.TextField(max_length=100)

#
# class ActivityMessageUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     message = models.ForeignKey(ActivityMessageMaster, on_delete=models.CASCADE)
