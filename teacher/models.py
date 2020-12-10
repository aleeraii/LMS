from django.db import models
from accounts.models import User


class TeacherModel(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    pay = models.IntegerField()
    leaves = models.IntegerField()
    date_joining = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
