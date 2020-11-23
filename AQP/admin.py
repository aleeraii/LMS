from django.contrib import admin
from .models import AssignmentModel, QuizModel, ExamModel
# Register your models here.

admin.site.register(AssignmentModel)
admin.site.register(QuizModel)
admin.site.register(ExamModel)
