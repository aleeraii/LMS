from django.db import models
from school_class.models import ClassModel
from subject.models import SubjectModel
# Create your models here.


class SectionModel(models.Model):

    section_name = models.CharField(max_length=5)
    class_id = models.ForeignKey(ClassModel, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(SubjectModel)

    def __str__(self):

        return self.class_id.class_grade + " " + self.section_name
