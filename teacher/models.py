from django.db import models
from accounts.models import User
from school_class.models import ClassModel
from subject.models import SubjectModel
from django.contrib.postgres.fields import ArrayField


class TeacherModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pay = models.IntegerField()
    leaves = models.IntegerField()
    date_joining = models.DateTimeField(auto_now_add=True)
    subjects = models.ManyToManyField(SubjectModel, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class TeacherContentModel(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    grade = models.ForeignKey(ClassModel, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE, null=True, blank=True)

