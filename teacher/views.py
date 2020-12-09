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
from queries.models import QueriesModel
from accounts.models import User
from django.views.generic import CreateView
from .forms import AddNotesForm, AddLectureForm, AddAssignmentForm, AddQuizForm, AddExamsForm, AddTodoForm
import datetime
roles = ['Dashboard', 'Content', 'Attendence', 'Classes', 'Lectures', 'Assignment', 'Quiz',
         'Exam', 'Timetable', 'Todo', 'Queries', 'Notes']


def dashboard(request):
    # INFO
    teacher_data = TeacherModel.objects.get(user=request.user)
    # NOTICE BOARD
    notices = NoticeBoardModel.objects.filter(user_group=request.user.user_role)
    # TO-DO
    todos = TodoModel.objects.filter(assign_to=request.user)
    tasks = []
    for task in todos:
        if task.date.day == datetime.date.today().day:
            tasks.append(task)
    # ATTENDANCE
    teacher = TeacherModel.objects.get(user=request.user)
    # IMPORTANT ! Should change the logic below on section part if one teacher is class teacher of only one class.
    # Current Logic: One teacher can be class teacher of multiple classes
    sections = SectionModel.objects.filter(class_teacher=teacher)
    total_students = 0
    present = 0
    absent = 0
    mark_attendance = True
    section = sections[0]
    for section in sections:
        student = StudentModel.objects.filter(section=section)
        for stu in student:
            attendance = AttendanceModel.objects.filter(user_id=stu.user)
            total_students += 1
            for attend in attendance:
                if attend.date_time.date() == datetime.datetime.now().date():
                    if attend.status == "Present":
                        present += 1
                    elif attend.status == 'Absent':
                        absent += 1
                    mark_attendance = False
    context = {
        'roles': roles,
        'notices': notices,
        'teacher_data': teacher_data,
        'todos': tasks,
        'mark_attendance': mark_attendance,
        "total_students": total_students,
        "present": present,
        "absent": absent,
        "section": section,
    }
    return render(request, "teacher/dashboard.html", context=context)


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
    if request.method == 'POST':
        form = AddTodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher:todo')
    else:
        form = AddTodoForm
    todos = TodoModel.objects.filter(assign_to=request.user)
    return render(request, "teacher/todo.html", context={'roles': roles, 'todo': todos, 'form': form})


def queries(request):
    query = QueriesModel.objects.filter(asked_to=request.user)
    ##########
    data_dict = dict()
    for que in query:
        if que.asked_by in data_dict.keys() and que.asked_to == request.user:
            if que.subject not in data_dict[que.asked_by]:
                data_dict[que.asked_by].append(que.subject)
        elif que.asked_by not in data_dict.keys() and que.asked_to == request.user:
            data_dict[que.asked_by] = [que.subject]
    return render(request, "teacher/queries.html", context={'roles': roles, 'queries': query, 'data': data_dict, })


def ask_query(request, id):
    if request.method == 'POST':
        file = request.FILES.get('myfile', None)
        message = request.POST.get("message")
        subject = request.POST.get("subject")
        asked_to = request.user
        asked_by = User.objects.get(id=id)
        status = request.POST.get("query_status")
        if status == "0":
            query_status = False
        elif status == None:
            query_status = True
        else:
            query_status = True
        if file is not None:
            form = QueriesModel(
                asked_by=asked_by,
                asked_to=asked_to,
                subject=subject,
                date_time=datetime.datetime.now(),
                chat=message,
                image=file,
                status='Response',
                query_status=query_status,

            )
        else:
            form = QueriesModel(
                asked_by=asked_by,
                asked_to=asked_to,
                subject=subject,
                date_time=datetime.datetime.now(),
                chat=message,
                status='Response',
                query_status=query_status,

            )
        form.save()
        return redirect("teacher:queries")
    return render(request, 'teacher/queries.html', {'roles': roles})


def timetable(request):
    teacher = TeacherModel.objects.get(user=request.user)
    sections = SectionModel.objects.filter(class_teacher=teacher)
    timetables = []
    data = TimeTableModel.objects.all()
    for d in data:
        for sect in sections:
            if sect == d.assign_to:
                timetables.append(d)

    return render(request, "teacher/timetable.html", context={'roles': roles, 'timetable': timetables})


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


def delete_assignment(request, id):
    obj = AssignmentModel.objects.get(id=id)
    obj.delete()
    return redirect("teacher:assignments")


def delete_exam(request, id):
    obj = ExamModel.objects.get(id=id)
    obj.delete()
    return redirect("teacher:exams")


def delete_quiz(request, id):
    obj = QuizModel.objects.get(id=id)
    obj.delete()
    return redirect("teacher:quiz")


def delete_notes(request, id):
    obj = NotesModel.objects.get(id=id)
    obj.delete()
    return redirect("teacher:notes")


def mark_todo(request, id):
    obj = TodoModel.objects.get(id=id)
    obj.delete()
    return redirect("teacher:todo")

