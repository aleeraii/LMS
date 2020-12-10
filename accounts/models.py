from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


USER_ROLES = (
    ('Student', 'Student'),
    ('Teacher', 'Teacher'),
    ('Parent', 'Parent'),
    ('Principal', 'Principal'),
    ('Owner', 'Owner'),
    ('Admin', 'Admin'),
)


class User(AbstractUser):
    user_role = models.CharField(
        max_length=10, choices=USER_ROLES, default="Admin")
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.username + ' ' + self.user_role
