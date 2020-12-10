from django.contrib import admin
from .models import NoticeBoardModel, NoticeBoardChoice
from django_summernote.admin import SummernoteModelAdmin


class NoticeboardAdmin(SummernoteModelAdmin):
    summernote_fields = ('notice',)


admin.site.register(NoticeBoardChoice)
admin.site.register(NoticeBoardModel, NoticeboardAdmin)
