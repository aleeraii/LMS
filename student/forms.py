from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from noticeboard.models import NoticeBoardModel
# # Apply summernote to specific fields.
# GROUPS_CHOICES = (
#     ('Teacher', 'Teacher'),
#     ('Student', 'Student'),
#     ('Owner', 'Owner'),
# )


class NoticeboardForm(forms.ModelForm):
    class Meta:
        model = NoticeBoardModel
        exclude = ['user', 'user_id', 'is_approve']
        widgets = {
            'notice': SummernoteWidget(),
        }
