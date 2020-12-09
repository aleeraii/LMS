from django import forms
from lecture.models import LectureModel
from notes.models import NotesModel
from AQP.models import AssignmentModel, QuizModel, ExamModel
from todo.models import TodoModel


class AddLectureForm(forms.ModelForm):
    class Meta:
        model = LectureModel
        fields = ('title', 'subject', 'lecture_file', 'teacher', 'section')


class AddNotesForm(forms.ModelForm):
    class Meta:
        model = NotesModel
        fields = ('title', 'subject', 'notes_file', 'teacher', 'section')


class AddQuizForm(forms.ModelForm):
    class Meta:
        model = QuizModel
        fields = '__all__'


class AddAssignmentForm(forms.ModelForm):
    class Meta:
        model = AssignmentModel
        fields = '__all__'


class AddExamsForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields = '__all__'


class DateInput(forms.DateInput):
    input_type = 'date'


class AddTodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }


# STATUSES = (
#     ('Question', 'Question'),
#     ('Response', 'Response'),
# )
#
#
# class SendQuery(forms.Form):
#     asked_by = forms.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
#     asked_to = forms.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
#     subject = forms.CharField(max_length=50, null=True, blank=True)
#     date_time = forms.DateTimeField(auto_now_add=True)
#     chat = forms.TextField()
#     image = forms.FileField(upload_to='queries/', null=True, blank=True)
#     status = forms.CharField(max_length=10, choices=STATUSES, default="Question")