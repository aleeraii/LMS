from django.db import models
from accounts.models import User


class OwnerModel(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    date_of_owning = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
