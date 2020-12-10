from django.db import models
from accounts.models import User
# Notification:
# Text
# Link
# Date/Time
# User-ID


class NotificationModel(models.Model):

    title = models.CharField(max_length=500)
    link = models.URLField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):

        return str(self.title) + ' ' + str(self.user)
