from django.db import models
from accounts.models import User
# Create your models here.
# NoticeBoard:
# NoticeID - Str
# NoticeTitle - Str
# NoticeFile - File
# UserID - ForeignKey (UID)
# UserGroup - Array Of String (Choice)
# DateTime - DateTime
# Approved - bool

MY_CHOICES = (
    ('Teacher', 'Teacher'),
    ('Student', 'Student'),
    ('Parent', 'Parent'),
    ('Principal', 'Principal'),
    ('Owner', 'Owner'),
    ('Admin', 'Admin'),

)


class NoticeBoardModel(models.Model):
    title = models.CharField(max_length=500)
    notice_file = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_group = models.CharField(max_length=9, choices=MY_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title) + " " + str(self.user) + " " + str(self.user_group)
