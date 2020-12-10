from django.db import models
from school.models import SchoolModel
# Create your models here.


class ClassModel(models.Model):
    class_grade = models.CharField(max_length=50, null=True)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_grade
