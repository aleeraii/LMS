from django.db import models
from accounts.models import User
from parent.models import ParentModel
from section.models import SectionModel
from school.models import SchoolModel
# Create your models here.


class StudentModel(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    parent = models.ForeignKey(
        ParentModel, null=True, blank=True, on_delete=models.CASCADE)
    section = models.ForeignKey(SectionModel, on_delete=models.CASCADE)
    leaves = models.IntegerField()
    date_joining = models.DateTimeField(auto_now_add=True)
    school = models.ForeignKey(
        SchoolModel, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
