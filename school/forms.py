from django import forms
from .models import SchoolModel


class SchoolForm(forms.ModelForm):

    class Meta:
        model = SchoolModel
        fields = ('name', 'address', 'student_function', 'teacher_function',
                  'parent_function', 'principal_function', 'owner_function', 'admin_function')
