from django.db import models
from accounts.models import User


class TimeTableModel(models.Model):
    assign_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    assign_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    image = models.ImageField(upload_to='images/')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
