from django.db import models
from accounts.models import User

# Create your models here.


class ParentModel(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.user)
