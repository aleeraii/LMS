from django.db import models
from accounts.models import User


class TodoModel(models.Model):
    assign_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    assign_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    task = models.CharField(max_length=500)
    date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True)


