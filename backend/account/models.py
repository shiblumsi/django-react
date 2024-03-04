from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
