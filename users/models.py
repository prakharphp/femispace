from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from master.models import TagMaster

# Create your models here.


class Gender(models.IntegerChoices):
    Male = 1
    Female = 2
    Other = 3
#
# #
# # class User(AbstractUser):
# #     tag = models.ManyToManyField(TagMaster, blank=True)
# #     gender = models.PositiveSmallIntegerField(choices=Gender.choices, default=Gender.Male)
#
#
# class AppUserManager(BaseUserManager):
#
#     def create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('The Email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, email, password, **extra_fields):
#
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         return self.create_user(email, password, **extra_fields)
# #


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
    id = models.UUIDField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField( max_length=150, blank=False, null=False)
    last_name = models.CharField( max_length=150, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=False)
    tag = models.ManyToManyField(TagMaster, blank=True)
    gender = models.PositiveSmallIntegerField(choices=Gender.choices, default=Gender.Male)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'tag', 'gender']

    # objects = AppUserManager()

    def _str_(self):
        return self.email