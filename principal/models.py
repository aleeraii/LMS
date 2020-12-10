from django.db import models
from accounts.models import User
# Create your models here.


class PrincipalModel(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    qualification = models.CharField(max_length=500, null=True)
    pay = models.IntegerField(null=True)
    joining_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
