from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.edit import FormView
from django.contrib import messages

# Create your views here.
from .forms import SignUpForm, SignInForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def signIn(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username,
                                password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, 'successfully login')
                if user.user_role == 'Teacher':
                    return redirect('teacher:dashboard')
                elif user.user_role == 'Student':
                    return redirect('student:dashboard')
                elif user.user_role == 'Parent':
                    return redirect('parent:dashboard')
                # elif user.user_role =="Owner":

            else:
                messages.error(
                    request, 'Please enter correct username and password combination')
                return redirect('login')
    else:
        form = SignInForm()
    return render(request, 'accounts/login.html', {'form': form})
