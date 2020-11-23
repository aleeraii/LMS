from django import forms
from lecture.models import LectureModel
from notes.models import NotesModel
from AQP.models import AssignmentModel, QuizModel, ExamModel


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

