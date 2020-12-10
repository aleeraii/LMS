from django.db import models
from section.models import SectionModel
from teacher.models import TeacherModel
# Create your models here.


class TimetableModel(models.Model):
    assign_to = models.OneToOneField(
        SectionModel, blank=True, null=True, on_delete=models.CASCADE)
    assign_by = models.ForeignKey(
        TeacherModel, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='timetable/')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.assign_to, self.assign_by)
