from django.shortcuts import render
from .forms import SchoolForm
from django.contrib import messages
# Create your views here.


def schoolView(request):
    if request.method == "POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO,
                                 'School is successfully created')
            return render(request, 'school/school_created.html')
    else:
        form = SchoolForm()
    return render(request, 'school/school_create.html', {'form': form})
