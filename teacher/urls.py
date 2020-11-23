from django.urls import path, reverse
from .views import dashboard, notes, lectures, exams, assignments, quiz, attendance, content, students, todo, timetable, mark_attendance, delete_lecture
from lecture.models import LectureModel
app_name = 'teacher'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('attendance/', attendance, name='attendance'),
    path('notes/', notes, name='notes'),
    path('quiz/', quiz, name='quiz'),
    path('assignments/', assignments, name='assignments'),
    path('exams/', exams, name='exams'),
    path('lectures/', lectures, name='lectures'),
    # path('add_lecture/', add_lectures_view, name='add_lecture'),
    # path('add_notes/', add_notes_view, name='add_notes'),
    # path('add_assignment/', add_assignment_view, name='add_assignment'),
    # path('add_quiz/', add_quiz_view, name='add_quiz'),
    # path('add_exam/', add_exams_view, name='add_exams'),
    path('content/', content, name='content'),
    path('students/', students, name='students'),
    path('todo/', todo, name='todo'),
    path('timetable/', timetable, name='timetable'),
    path('mark_attendance/', mark_attendance, name='mark_attendance'),
    path('delete/', delete_lecture, name='delete_lecture'),
]
