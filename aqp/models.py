from django.db import models
from subject.models import SubjectModel
from section.models import SectionModel
from teacher.models import TeacherModel
from student.models import StudentModel
# Create your models here.

CHOICES = (
    ("Assignment", "Assignment"),
    ("Quiz", "Quiz"),
    ("Paper", "Paper"),
)


class AssignmentQuizPaperModel(models.Model):
    title = models.CharField(max_length=300, null=False)
    which_type = models.CharField(
        max_length=10, choices=CHOICES, default="Assignment")
    assignment_file = models.FileField(upload_to='teacher/assignment/')
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)
    section = models.ForeignKey(SectionModel, on_delete=models.CASCADE)
    due_date = models.DateTimeField(auto_now_add=True)
    total_marks = models.IntegerField()
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class SubmissionModel(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    answer = models.FileField(upload_to='student/assignment/')
    marks_obtained = models.IntegerField()
    marked = models.BooleanField(default=False)
    remarks = models.CharField(max_length=500)
    assignment = models.ForeignKey(
        AssignmentQuizPaperModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student) + ' ' + str(self.marked)

# AssignmentID - Str
# AssignmentTitle - Str
# AssignmentFile - File
# AssignmentSubject - Str
# PublishDateTime - DateTime
# DueDateTime - DateTime
# TotalMarks - Int
# Class { ClassID - ForeignKey (CID) }
# Submission { StudentID - ForeignKey (SID), AnswerUpload - File, MarksObtained - INT, Remarks : Str }
