from django.db import models
from django.shortcuts import reverse
from subject.models import SubjectModel
from teacher.models import TeacherModel
from section.models import SectionModel
# Create your models here.
# Lecture:
# LectureID - Str
# LectureTitle - Str
# LectureSubject - Str
# LectureFile - File
# DateTime - DateTime
# TeacherID - ForiegnKey (TID)
# ClassID - ForeignKey (CID)

roles = ['Dashboard', 'Content', 'Attendence', 'Classes', 'Lectures', 'Assignment', 'Quiz',
         'Exam', 'Timetable', 'Todo', 'Queries', 'Notes']


class LectureModel(models.Model):
    title = models.CharField(max_length=100)
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)
    lecture_file = models.FileField(upload_to='teacher/lectures', null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE)
    section = models.ForeignKey(SectionModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

