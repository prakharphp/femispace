from django.db import models
from food.models import Meal, Food
from master.models import TagMaster
from users.models import User


class ActivityMaster(models.Model):
    title = models.CharField(verbose_name="Activity Title", max_length=100)
    tag = models.ManyToManyField(TagMaster, blank=True)

    def __str__(self):
        return self.title


class ExerciseMaster(models.Model):
    title = models.CharField(verbose_name="Exercise Title", max_length=100)
    category = models.CharField(verbose_name="Exercise Category", max_length=100, blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    image_link = models.URLField(blank=True, null=True)
    duration_min = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.title


class ExerciseActivityMaster(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    exercise = models.ManyToManyField(ExerciseMaster, blank=True)
    duration_min = models.PositiveSmallIntegerField(blank=True, null=True)
    calories_burn = models.PositiveIntegerField(blank=True, null=True)
    tag = models.ManyToManyField(TagMaster, blank=True)

    def __str__(self):
        return '%s' % self.name


class Day(models.Model):
    title = models.CharField(max_length=50)
    activity = models.ManyToManyField(ActivityMaster, blank=True)
    breakfast_meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, blank=True, related_name="breakfast")
    brunch_meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, blank=True, related_name="brunch")
    lunch_meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, blank=True, related_name="lunch")
    eve_snacks_meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, blank=True, related_name="eve_snack")
    dinner_meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, blank=True, related_name="dinner")
    morning_exercise = models.ManyToManyField(ExerciseMaster, blank=True, related_name="morning_exercise_list")
    evening_exercise = models.ManyToManyField(ExerciseMaster, blank=True, related_name="evening_exercise_list")
    tag = models.ManyToManyField(TagMaster, blank=True)

    def __str__(self):
        return self.title


class EatRainbowMaster(models.Model):
    title = models.CharField(max_length=50)
    red_serving = models.PositiveSmallIntegerField(default=0)
    cream_serving = models.PositiveSmallIntegerField(default=0)
    yellow_serving = models.PositiveSmallIntegerField(default=0)
    kiwi_serving = models.PositiveSmallIntegerField(default=0)
    blue_serving = models.PositiveSmallIntegerField(default=0)
    green_serving = models.PositiveSmallIntegerField(default=0)
    enjoy_regular = models.ManyToManyField(Food, blank=True, related_name="enjoy_regular_master")
    eat_more = models.ManyToManyField(Food, blank=True, related_name="eat_more_master")
    eat_less = models.ManyToManyField(Food, blank=True, related_name="eat_less_master")
    eat_avoid = models.ManyToManyField(Food, verbose_name="Avoid eat", blank=True, related_name="eat_avoid_master")
    tag = models.ManyToManyField(TagMaster, blank=True)


class EatRainbowActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
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


class DrinkingActivityMaster(models.Model):
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
    fruit = models.ManyToManyField(Food, blank=True, related_name="fruit_user")
    dried_fruit = models.ManyToManyField(Food, blank=True, related_name="dry_fruit_user")
    sweet_veggies = models.ManyToManyField(Food, blank=True, related_name="sweet_vaggies_user")
    drink_juice = models.ManyToManyField(Food, blank=True, related_name="drink_juice_user")
    dessert_snacks = models.ManyToManyField(Food, blank=True, related_name="dessert_snacks_user")
    sugar_consumed = models.PositiveSmallIntegerField(default=0)
    calories_gained = models.PositiveSmallIntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    tag = models.ManyToManyField(TagMaster, blank=True)


class SugarIntakeActivityMaster(models.Model):
    fruits = models.ManyToManyField(Food, blank=True, related_name="fruits")
    dried_fruits = models.ManyToManyField(Food, blank=True, related_name="Dry_Fruits")
    sweet_veggie = models.ManyToManyField(Food, blank=True, related_name="sweet_vaggies")
    drink_juices = models.ManyToManyField(Food, blank=True, related_name="drink_juice")
    dessert_snack = models.ManyToManyField(Food, blank=True, related_name="dessert_snacks")
    sugar_intake = models.PositiveSmallIntegerField(default=0)
    calories_gained = models.PositiveSmallIntegerField(default=0)
    comments = models.TextField(blank=True, null=True)


class MeditationMaster(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    url = models.URLField()
    Description = models.TextField()


class MeditationActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    meditation = None


class Program(models.Model):
    title = models.CharField(max_length=50)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    days = models.ManyToManyField(Day)
    preferred_for = models.ManyToManyField('health.WellnessArea', blank=True)
    tag = models.ManyToManyField(TagMaster, blank=True)
    duration_in_days = models.CharField(max_length=50, default=7)
    # start_date = models.DateField()
    eat_rainbow = models.ForeignKey(EatRainbowMaster, on_delete=models.CASCADE, blank=True, null=True)
    exercise = models.ForeignKey(ExerciseActivityMaster, on_delete=models.CASCADE, blank=True, null=True)
    drinking_exercise = models.ForeignKey(DrinkingActivityMaster, on_delete=models.CASCADE, blank=True, null=True)
    sugar_intake = models.ForeignKey(SugarIntakeActivityMaster, on_delete=models.CASCADE, blank=True, null=True)
    meditation = models.ForeignKey(MeditationMaster, on_delete=models.CASCADE, blank=True, null=True)


    @property
    def day_count(self):
        return len(self.days.all()) if self.days else 0

    def __str__(self):
        return self.title


class UserPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    start_date = models.DateField()
    asssigned_date = models.DateField()


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