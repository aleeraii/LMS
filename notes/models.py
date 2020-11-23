from django.db import models
from subject.models import SubjectModel
from section.models import SectionModel
from teacher.models import TeacherModel
# Notes:
# NotesID - Str
# NotesTitle - str
# NotesFile - File
# Subject - Str
# ClassID - ForeignKey (CID)
# TeacherID - ForeignKey (TID)
# DatePublish - DateTime


class NotesModel(models.Model):
    title = models.CharField(max_length=100)
    notes_file = models.FileField(upload_to='teacher/notes', null=True, blank=True)
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)
    section = models.ForeignKey(SectionModel, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return str(self.title) + ' ' + str(self.teacher) + ' ' + str(self.section)
