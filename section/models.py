from django.db import models
from school_class.models import ClassModel
from subject.models import SubjectModel
from teacher.models import TeacherModel


class SectionModel(models.Model):
    section_name = models.CharField(max_length=5)
    class_id = models.ForeignKey(ClassModel, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(SubjectModel)
    # below field is assigned to get data in content and students view of teacher
    class_teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.class_id.class_grade + " " + self.section_name
