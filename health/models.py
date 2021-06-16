from django.db import models
from users.models import User
from master.models import TagMaster


class WellnessArea(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class MonthCycle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    is_menstruation = models.BooleanField(default=False)
    is_follicular = models.BooleanField(default=False)
    is_ovulation = models.BooleanField(default=False)
    is_luteal = models.BooleanField(default=False)
    is_pre_menstruation = models.BooleanField(default=False)
    is_actual = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    feeling = models.ManyToManyField('health.WellnessArea', blank=True)
    tag = models.ManyToManyField(TagMaster, blank=True)

    def __str__(self):
        return f"{self.user.username} on {self.date}"


class AverageCycle(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    menstruation_days = models.PositiveSmallIntegerField(default=5)
    follicular_days = models.PositiveSmallIntegerField(default=5)
    proliferative_days = models.PositiveSmallIntegerField(default=5)
    luteal_days = models.PositiveSmallIntegerField(default=5)
    secretory_days = models.PositiveSmallIntegerField(default=5)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}"

# include 5 activities with real
# ingedients in nutritions
# macros like carbs fat protine and total calories
# Alias names for ingredient names to find the nutritional values
# recipes in steps make 15
# tagging for days in phase in a days
# class Messages():
#class Lerning areas
#class exercise