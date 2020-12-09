from django.urls import path, reverse
from .views import dashboard, notes, lectures, exams, assignments, quiz, attendance, content, students, todo, timetable\
    , mark_attendance, delete_lecture, mark_todo, queries, ask_query, delete_assignment, delete_exam, delete_quiz, delete_notes
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
    path('content/', content, name='content'),
    path('students/', students, name='students'),
    path('todo/', todo, name='todo'),
    path('timetable/', timetable, name='timetable'),
    path('queries/', queries, name='queries'),
    path('ask_query/<int:id>', ask_query, name='ask_query'),
    path('mark_attendance/', mark_attendance, name='mark_attendance'),
    path('delete_lecture/<int:id>', delete_lecture, name='delete_lectures'),
    path('delete_assignment/<int:id>', delete_assignment, name='delete_assignments'),
    path('delete_exam/<int:id>', delete_exam, name='delete_exams'),
    path('delete_quiz/<int:id>', delete_quiz, name='delete_quiz'),
    path('delete_notes/<int:id>', delete_notes, name='delete_notes'),
    path('mark_todo/<int:id>', mark_todo, name='mark_todo'),
]
