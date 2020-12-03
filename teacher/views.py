import datetime
from django.shortcuts import render, redirect
from noticeboard.models import NoticeBoardModel
from AQP.models import AssignmentModel, QuizModel, ExamModel
from notes.models import NotesModel
from lecture.models import LectureModel
from section.models import SectionModel
from student.models import StudentModel
from school_class.models import ClassModel
from attendance.models import AttendanceModel
from teacher.models import TeacherModel, TeacherContentModel
from timetable.models import TimeTableModel
from todo.models import TodoModel
from django.views.generic import CreateView
from .forms import AddNotesForm, AddLectureForm, AddAssignmentForm, AddQuizForm, AddExamsForm
import datetime
roles = ['Dashboard', 'Content', 'Attendence', 'Classes', 'Lectures', 'Assignment', 'Quiz',
         'Exam', 'Timetable', 'Todo', 'Queries', 'Notes']


def dashboard(request):
    # INFO
    teacher_data = TeacherModel.objects.all()
    # NOTICE BOARD
    notices = NoticeBoardModel.objects.all()
    # TO-DO
    todos = TodoModel.objects.filter(assign_to=request.user)
    tasks = []
    for task in todos:
        if task.date.day == datetime.date.today().day:
            tasks.append(task)
    # ATTENDANCE
    attendance = AttendanceModel.objects.all()

    return render(request, "teacher/dashboard.html", context={'roles': roles, 'notices': notices, 'teacher_data': teacher_data, 'todos': tasks})


def notes(request):
    if request.method == 'POST':
        form = AddNotesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher:notes')
    else:
        form = AddNotesForm()
    note = NotesModel.objects.all()
    return render(request, "teacher/notes.html", context={'roles': roles, 'notes': note, 'form': form})


def quiz(request):
    if request.method == 'POST':
        form = AddQuizForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher:quiz')
    else:
        form = AddQuizForm
    quiz = QuizModel.objects.all()
    return render(request, "teacher/quiz.html", context={'roles': roles, 'quiz': quiz, 'form': form})


def assignments(request):
    if request.method == 'POST':
        form = AddAssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher:assignments')
    else:
        form = AddAssignmentForm
    assignment = AssignmentModel.objects.all()
    return render(request, "teacher/assignments.html", context={'roles': roles, 'assignments': assignment, 'form': form})


def exams(request):
    if request.method == 'POST':
        form = AddExamsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher:exams')
    else:
        form = AddExamsForm
    exam = ExamModel.objects.all()
    return render(request, "teacher/exams.html", context={'roles': roles, 'exams': exam, 'form': form})


def lectures(request):
    if request.method == 'POST':
        form = AddLectureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher:lectures')
    else:
        form = AddLectureForm
    lecture = LectureModel.objects.all()
    return render(request, "teacher/lectures.html", context={'roles': roles, 'lectures': lecture, 'form': form})


def content(request):
    teacher = TeacherModel.objects.get(user=request.user)
    sections = SectionModel.objects.filter(class_teacher=teacher)
    album = TeacherContentModel.objects.all()
    classes = {}
    for section in sections:
        if section.class_id in classes.keys():
            pass
        else:
            sub = []
            for subject in section.subjects.all():
                sub.append(subject.name)
            classes[section.class_id] = sub
    subjects = teacher.subjects.all()
    videos = []
    for video in album:
        if video.grade in classes.keys():
            videos.append(video)
    return render(request, "teacher/content.html", context={'roles': roles, 'videos': videos, 'classes': classes, 'subjects': subjects, 'sections': sections})


def students(request):
    teacher = TeacherModel.objects.get(user=request.user)
    sections = SectionModel.objects.filter(class_teacher=teacher)
    students = StudentModel.objects.all()
    # for section in sections:
    #     for student in students:
    #         if student.section == section:
    #             print(student.user.username)
    return render(request, "teacher/students.html",
                  context={'roles': roles, 'sections': sections, 'students': students})


def todo(request):
    todos = TodoModel.objects.filter(assign_to=request.user)
    return render(request, "teacher/todo.html", context={'roles': roles, 'todo': todos})


def timetable(request):
    timetable = TimeTableModel.objects.all()
    return render(request, "teacher/timetable.html", context={'roles': roles, 'timetable': timetable})


def attendance(request):
    teacher = TeacherModel.objects.get(user=request.user)
    sections = SectionModel.objects.filter(class_teacher=teacher)
    student_list = []
    mark_attendance = True
    for section in sections:
        student = StudentModel.objects.filter(section=section)
        for stu in student:
            student_list.append(stu)
            attendance = AttendanceModel.objects.filter(user_id=stu.user)
            for attend in attendance:
                if attend.date_time.date() == datetime.datetime.now().date():
                    mark_attendance = False
    print(mark_attendance)

    return render(request, "teacher/attendance.html", context={'roles': roles, 'sections': sections, 'students': student_list, 'mark_attendance': mark_attendance})


def mark_attendance(request):
    teacher = TeacherModel.objects.get(user=request.user)
    sections = SectionModel.objects.filter(class_teacher=teacher)
    student_list = []
    for section in sections:
        student = StudentModel.objects.filter(section=section)
        for stu in student:
            student_list.append(stu)
    if request.method == 'POST':
        for stud in student_list:
            status = request.POST.get(str(stud.user.username))
            form = AttendanceModel(
                date_time=datetime.datetime.now(),
                status=status,
                user_id=stud.user,
                section=stud.section
            )
            form.save()
        return redirect('teacher:attendance')
    return render(request, 'teacher/attendance.html', {'roles': roles})


def delete_lecture(request, id):
    obj = LectureModel.objects.get(id=id)
    obj.delete()
    return redirect("teacher:lectures")