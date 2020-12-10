from django.views.generic.base import TemplateView

# Create your views here.


class DashboardView(TemplateView):
    template_name = 'Parent/parent_dashboard.html'


class AttendanceView(TemplateView):
    template_name = "Parent/parent_attendance.html"
