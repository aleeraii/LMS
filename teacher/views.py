from django.shortcuts import render

# Create your views here.


def dashboardView(request):
    roles = ['Dashboard', 'Lectures']
    return render(request, 'dashboard.html', context={'roles': roles})
