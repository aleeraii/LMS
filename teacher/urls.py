from django.urls import path
from .views import dashboardView
app_name = 'teacher'
urlpatterns = [
    path('dashboard/', dashboardView, name="dashboard")
]
