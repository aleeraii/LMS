from django.urls import path
from .views import(dashboardView, notesView, lecturesView, noticeboardView, feechallanView,
                   attendanceView, assignmentView, notesView, timetableView, resultView, paperView, quizView)

app_name = 'student'


urlpatterns = [
    path('dashboard/', dashboardView, name="dashboard"),
    path('notes/', notesView, name="notes"),
    path('lectures/', lecturesView, name='lectures'),
    path('feechallan/', feechallanView, name='feechallan'),
    path('attendance/', attendanceView, name='attendance'),
    path('assignment/', assignmentView, name='assignment'),
    path('quiz/', quizView, name='quiz'),
    path('paper/', paperView, name='paper'),
    path('notes/', notesView, name='notes'),
    path('noriceboard/', noticeboardView, name='noticeboard'),
    path('timetable/', timetableView, name='timetable'),
    path('result/', resultView, name='result'),
]
