from django.db import models
from subject.models import SubjectModel
from section.models import SectionModel
from teacher.models import TeacherModel
# Create your models here.


class AssignmentModel(models.Model):
    title = models.CharField(max_length=300)
    assignment_file = models.FileField(upload_to='teacher/assignments', null=True, blank=True)
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)
    section = models.ForeignKey(SectionModel, on_delete=models.CASCADE)
    due_date = models.DateTimeField(auto_now_add=True)
    total_marks = models.IntegerField()
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class QuizModel(models.Model):
    title = models.CharField(max_length=300)
    file = models.FileField(upload_to='teacher/quiz', null=True, blank=True)
    subject = models.ForeignKey(SubjectModel, on_delete = models.CASCADE)
    section = models.ForeignKey(SectionModel, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_marks = models.IntegerField()
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class ExamModel(models.Model):
    title = models.CharField(max_length=300)
    exam_file = models.FileField(upload_to='teacher/exams', null=True, blank=True)
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)
    section = models.ForeignKey(SectionModel, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_marks = models.IntegerField()
    teacher = models.ForeignKey(TeacherModel, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.title)
