from django.db import models
from accounts.models import User
from parent.models import ParentModel
from section.models import SectionModel
# Create your models here.


class StudentModel(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    parent = models.ForeignKey(ParentModel, on_delete=models.CASCADE)
    section = models.ForeignKey(SectionModel, on_delete=models.CASCADE)
    leaves = models.IntegerField()
    date_joining = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
