from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from master.models import TagMaster

# Create your models here.


class Gender(models.IntegerChoices):
    Male = 1
    Female = 2
    Other = 3


class AppUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        extra_fields.pop('tag')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_set_group",
        related_query_name="user_group_query",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="user_set_permissions",
        related_query_name="user_permissions_query",
    )
    username = None
    # id = models.UUIDField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField( max_length=150, blank=False, null=False)
    last_name = models.CharField( max_length=150, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=False)
    tag = models.ManyToManyField(TagMaster, blank=True)
    gender = models.PositiveSmallIntegerField(choices=Gender.choices, default=Gender.Male)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'tag', 'gender']

    objects = AppUserManager()

    def _str_(self):
        return self.email
#Pop up for user


class Mood(models.IntegerChoices):

    Good = 1
    Bad = 2
    Other = 3


class TestChoice(models.IntegerChoices):
    Not_available = 1
    Positive = 2
    Negative = 3


class TestChoiceLevel(models.IntegerChoices):
    Not_available = 1
    Low = 2
    Medium = 3
    High = 4


class FerningChoices(models.IntegerChoices):
    Not_available = 1
    none = 2
    Partial = 3
    Full = 4


class IvfChoices(models.IntegerChoices):
    Not_available = 1
    Retrieval = 2
    transfer = 3
    freezing = 4


class InserminationChoices(models.IntegerChoices):
    Not_available = 1
    IUI = 2
    ICSI = 3
    IVI = 4
    HCG = 5
    HSG_Exam = 6
    SHG_Exam = 7


class UserHealth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_period_started = models.BooleanField(default=False)
    is_ovulation = models.BooleanField(default=False)
    temperature = models.PositiveSmallIntegerField()
    temperature_unit = models.CharField(max_length= 5)
    weight = models.PositiveSmallIntegerField()
    weight_unit = models.CharField(max_length= 5)
    sleep_min = models.IntegerField()
    mood = models.PositiveSmallIntegerField(choices=Mood.choices, default=Mood.Good)
    cervical_fluid = models.CharField(max_length=10)
    period = models.CharField(verbose_name= 'period/spotting', max_length=10)

    test_devices_Std_Opk = models.PositiveSmallIntegerField(choices=TestChoice.choices, default=TestChoice.Not_available)
    Advance_Opk = models.PositiveSmallIntegerField(choices=TestChoiceLevel.choices, default=TestChoiceLevel.Not_available)
    pregnancy_test = models.PositiveSmallIntegerField(choices=TestChoice.choices, default=TestChoice.Not_available)
    Blood = models.PositiveSmallIntegerField(choices=TestChoice.choices, default=TestChoice.Not_available)
    progesterone_test = models.PositiveSmallIntegerField(choices=TestChoice.choices, default=TestChoice.Not_available)

    Ferning_Microscope = models.PositiveSmallIntegerField(choices=FerningChoices.choices, default=FerningChoices.Not_available)
    ivf = models.PositiveSmallIntegerField(choices=IvfChoices.choices, default=IvfChoices.Not_available)
    Insermination = models.PositiveSmallIntegerField(choices=InserminationChoices.choices, default=InserminationChoices.Not_available)

    osteoporosis = models.DateField()
    heart_disease = models.DateField()
    from_uninary_incontinence_diabetes = models.DateField()
    to_uninary_incontinence_diabetes = models.DateField()
    stroke = models.DateField()

    biomaker_result =models.PositiveSmallIntegerField()
    biomaker_result_unit = models.CharField(max_length=10)
    biomaker_date = models.DateField()
    biomaker_result_period_day = models.CharField(max_length=5, default=0)
    progesterone_result = models.PositiveSmallIntegerField()
    progesterone_result_unit = models.CharField(max_length=10)
    progesterone_date = models.DateField()
    progesterone_result_period_day = models.CharField(max_length=5, default=0)

    comment = models.TextField(max_length=200)
    symptoms_conditions = models.ManyToManyField(TagMaster, blank=True)
