from django.shortcuts import render, redirect
from notes.models import NotesModel
from section.models import SectionModel
from lecture.models import LectureModel
from noticeboard.models import NoticeBoardModel
from timetable.models import TimetableModel
from aqp.models import AssignmentQuizPaperModel
from django.contrib.auth.decorators import login_required
from .forms import NoticeboardForm


@login_required(login_url='login')
def dashboardView(request):

    return render(request, 'Student/student_dashboard.html')


@login_required(login_url='login')
def notesView(request):
    section = request.user.studentmodel.section
    subjects = section.subjects.all()
    notesSectionWise = NotesModel.objects.filter(section=section)
    context = {
        'subjects': subjects,
        'notesSectionWise': notesSectionWise,
    }
    return render(request, 'Student/student_notes.html', context)


@login_required(login_url='login')
def lecturesView(request):
    section = request.user.studentmodel.section
    subjects = section.subjects.all()
    lecturesSectionWise = LectureModel.objects.filter(section=section)
    context = {
        'subjects': subjects,
        'lecturesSectionWise': lecturesSectionWise
    }
    return render(request, 'Student/student_lectures.html', context)


@login_required(login_url='login')
def assignmentView(request):
    assignments = AssignmentQuizPaperModel.objects.filter(which_type='')
    return render(request, 'Student/student_assignment.html')


def quizView(request):
    return render(request, 'Student/student_quiz.html')


def paperView(request):
    return render(request, 'Student/student_paper.html')


@login_required(login_url='login')
def attendanceView(request):
    return render(request, 'Student/student_attendance.html')


@login_required(login_url='login')
def feechallanView(request):
    return render(request, 'Student/student_feechallan.html')


@login_required(login_url='login')
def noticeboardView(request):
    if request.method == "POST":
        form = NoticeboardForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            notice = form.cleaned_data.get('notice')
            user_group = form.cleaned_data.get('user_group')
            noticeboard = NoticeBoardModel.objects.create(
                title=title, notice=notice, user=request.user)
            noticeboard.user_group.add(*user_group)
            noticeboard.save()
            return redirect('student:noticeboard')
    else:
        noticeboards = NoticeBoardModel.objects.filter(
            is_approve=True, user_group__title="Student")
        form = NoticeboardForm()
        context = {
            'noticeboards': noticeboards,
            'form': form,
        }
        return render(request, 'Student/student_noticeboard.html', context)


@ login_required(login_url='login')
def resultView(request):
    return render(request, 'Student/student_result.html')


@ login_required(login_url='login')
def timetableView(request):
    section = request.user.studentmodel.section
    timetable = section.timetablemodel
    context = {
        'section': section,
        'timetable': timetable,
    }
    return render(request, 'Student/student_timetable.html', context)
