from django.db import models
from accounts.models import User


STATUSES = (
    ('Question', 'Question'),
    ('Response', 'Response'),
)


class QueriesModel(models.Model):
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    asked_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    subject = models.CharField(max_length=50, null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    chat = models.TextField()
    image = models.FileField(upload_to='queries/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUSES, default="Question")
    query_status = models.BooleanField(default=1)
