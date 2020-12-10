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


class NoticeBoardChoice(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)


class NoticeBoardModel(models.Model):
    title = models.CharField(max_length=100)
    notice = models.CharField(max_length=10000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_group = models.ManyToManyField(NoticeBoardChoice)
    is_approve = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return str(self.title) + " Notice by " + str(self.user) + " For " + str(self.user_group.all())
