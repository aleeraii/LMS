from django.urls import path
from .views import DashboardView, AttendanceView

app_name = 'parent'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('attendance/', AttendanceView.as_view(), name='attendance'),
]
