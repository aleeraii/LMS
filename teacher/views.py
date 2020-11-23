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
from django.views.generic import CreateView
from .forms import AddNotesForm, AddLectureForm, AddAssignmentForm, AddQuizForm, AddExamsForm

roles = ['Dashboard', 'Content', 'Attendence', 'Classes', 'Lectures', 'Assignment', 'Quiz',
         'Exam', 'Timetable', 'Todo', 'Queries', 'Notes']


def dashboard(request):
    teacher_data = TeacherModel.objects.all()
    notices = NoticeBoardModel.objects.all()
    return render(request, "teacher/dashboard.html", context={'roles': roles, 'notices': notices, 'teacher_data': teacher_data})


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


# def add_notes_view(request):
#     if request.method == 'POST':
#         form = AddNotesForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('teacher:notes')
#     else:
#         form = AddNotesForm()
#
#     return render(request, 'teacher/add_notes_form.html', {'form': form, 'roles': roles})


# def add_lectures_view(request):
#     if request.method == 'POST':
#         form = AddLectureForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('teacher:lectures')
#     else:
#         form = AddLectureForm
#     return render(request, 'teacher/lectures_form.html', {'form': form, 'roles': roles})


# def add_assignment_view(request):
#     if request.method == 'POST':
#         form = AddAssignmentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('teacher:assignments')
#     else:
#         form = AddAssignmentForm
#     return render(request, 'teacher/add_assignment_form.html', {'form': form, 'roles': roles})


# def add_exams_view(request):
#     if request.method == 'POST':
#         form = AddExamsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('teacher:exams')
#     else:
#         form = AddExamsForm
#     return render(request, 'teacher/add_exams_form.html', {'form': form, 'roles': roles})


# def add_quiz_view(request):
#     if request.method == 'POST':
#         form = AddQuizForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('teacher:quiz')
#     else:
#         form = AddQuizForm
#     return render(request, 'teacher/add_quiz_form.html', {'form': form, 'roles': roles})


def content(request):
    teacher = TeacherModel.objects.get(user=request.user)
    sections = SectionModel.objects.filter(class_teacher=teacher)
    album = TeacherContentModel.objects.all()
    classes = []
    for section in sections:
        if section.class_id in classes:
            pass
        else:
            classes.append(section.class_id)
    return render(request, "teacher/content.html", context={'roles': roles, 'album': album, 'classes': classes})


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
    # exam = ExamModel.objects.all()
    return render(request, "teacher/todo.html", context={'roles': roles})


def timetable(request):
    timetable = TimeTableModel.objects.all()
    return render(request, "teacher/timetable.html", context={'roles': roles, 'timetable': timetable})


def attendance(request):
    teacher = TeacherModel.objects.get(user=request.user)
    sections = SectionModel.objects.filter(class_teacher=teacher)
    student_list = []
    for section in sections:
        student = StudentModel.objects.filter(section=section)
        for stu in student:
            student_list.append(stu)
    return render(request, "teacher/attendance.html", context={'roles': roles, 'sections': sections, 'students': student_list})


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


def delete_lecture(request, title=None):
    if title:
        obj = LectureModel.objects.get(title=title)
        obj.delete()
        return render(request, "teacher:lectures")
    else:
        print("Not Found")
        return render(request, "teacher:lectures")