from django.db import models
from master.models import *
from users.models import User


class EatRainbowActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    previous_date_data = models.ForeignKey(EatRainbowMaster, on_delete=models.CASCADE, blank=True, null=True)
    is_actual = models.BooleanField(default=False)
    red_serving = models.PositiveSmallIntegerField(default=0)
    cream_serving = models.PositiveSmallIntegerField(default=0)
    yellow_serving = models.PositiveSmallIntegerField(default=0)
    kiwi_serving = models.PositiveSmallIntegerField(default=0)
    blue_serving = models.PositiveSmallIntegerField(default=0)
    green_serving = models.PositiveSmallIntegerField(default=0)
    enjoy_regular = models.ManyToManyField(Food, blank=True, related_name="enjoy_regular_user")
    eat_more = models.ManyToManyField(Food, blank=True, related_name="eat_more_user")
    eat_less = models.ManyToManyField(Food, blank=True, related_name="eat_less_user")
    eat_avoid = models.ManyToManyField(Food, verbose_name="Avoid eat", blank=True, related_name="eat_avoid_user")
    tag = models.ManyToManyField(TagMaster, blank=True)
    comment = models.TextField(blank=True, null=True)


class FeelingAfterExercise(models.TextChoices):
    GREAT_AND_EASY = "GE"
    NORMAL = "NR"
    HARD = "HR"
    EXHAUSTED = "EX"
    SICK = "SI"


class ExerciseActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    is_actual = models.BooleanField(default=False)
    previous_date_data = models.ForeignKey(ExerciseActivityMaster, on_delete=models.CASCADE, blank=True, null=True)
    exercise = models.ManyToManyField(ExerciseMaster, blank=True)
    duration = models.PositiveSmallIntegerField(default=90)
    met = models.FloatField(default=0)
    calories = models.PositiveSmallIntegerField(default=200)
    feeling = models.CharField(max_length=2, choices=FeelingAfterExercise.choices, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    tag = models.ManyToManyField(TagMaster, blank=True)


class DrinkingWaterActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    previous_date_data = models.ForeignKey(DrinkingActivityMaster, on_delete=models.CASCADE, blank=True, null=True)
    is_actual = models.BooleanField(default=False)
    water = models.PositiveSmallIntegerField(default=5)
    soft_drink = models.PositiveSmallIntegerField(default=0)
    smoothie = models.PositiveSmallIntegerField(default=0)
    ice_tea = models.PositiveSmallIntegerField(default=0)
    fruit_juice = models.PositiveSmallIntegerField(default=0)
    coffee = models.PositiveSmallIntegerField(default=0)
    bear = models.PositiveSmallIntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    tag = models.ManyToManyField(TagMaster, blank=True)


class SugarIntakeActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    is_actual = models.BooleanField(default=False)
    previous_date_data = models.ForeignKey(SugarIntakeActivityMaster, on_delete=models.CASCADE, blank=True, null=True)
    fruit = models.ManyToManyField(Food, blank=True, related_name="fruit_user")
    dried_fruit = models.ManyToManyField(Food, blank=True, related_name="dry_fruit_user")
    sweet_veggies = models.ManyToManyField(Food, blank=True, related_name="sweet_vaggies_user")
    drink_juice = models.ManyToManyField(Food, blank=True, related_name="drink_juice_user")
    dessert_snacks = models.ManyToManyField(Food, blank=True, related_name="dessert_snacks_user")
    sugar_consumed = models.PositiveSmallIntegerField(default=0)
    calories_gained = models.PositiveSmallIntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    tag = models.ManyToManyField(TagMaster, blank=True)


class MeditationActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    previous_date_data = models.ForeignKey(MeditationMaster, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    meditation = None


class UserPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateField()
    asssigned_date = models.DateField()

    def __str__(self):
        return '%s' % self.user


class FrequencyChoices(models.IntegerChoices):
    Daily = 1
    Weekly = 2
    Monthly = 3


class AddCustomActivity(models.Model):
    category = models.ForeignKey(ActivityMaster, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=20)
    stat_date = models.DateField()
    duration_in_days = models.CharField(max_length=50)
    target_frequency = models.PositiveSmallIntegerField(choices=FrequencyChoices.choices, default=FrequencyChoices.Monthly)

    def __str__(self):
        return '%s' % self.activity_name



