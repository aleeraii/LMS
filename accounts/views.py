from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# Create your views here.
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def homeView(request):
    roles = ['Dashboard', 'Content', 'Attendence', 'Classes', 'Lectures', 'Assignment', 'Quiz',
             'Exam', 'Timetable', 'Todo', 'Queries', 'Notes']
    # roles = ['Dashboard', 'Content', 'Attendence', 'Time Table',
    #          'Student Info', 'Lectures', 'Assignment', 'Quiz', 'Paper', 'TO DO', 'Queries', 'Notes']

    return render(request, "teacher/dashboard.html", context={'roles': roles})
