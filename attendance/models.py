from django.db import models
from accounts.models import User
from section.models import SectionModel
# Create your models here.
# Attendance:
# DateTime - DateTime
# AttendanceFrameTime - Time
# Status - {Present, Absent, Leave}
# UserID - ForeignKey (UID)
# Leave pending (bool)
# Type Of leave (Choice -> medical others)

ATTENDANCE_STATUS = [
    ('Absent', 'Absent'),
    ('Present', 'Present'),
    ('Leave', 'Leave'),
]


class AttendanceModel(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=7, choices=ATTENDANCE_STATUS, default='Absent')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(SectionModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.status) + ' ' + str(self.user_id) + ' ' + str(self.section)

