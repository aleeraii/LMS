from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
    path('school/', include('school.urls')),
    path('parent/', include('parent.urls')),
    path('reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html',
                                                        email_template_name='accounts/password_reset_email.html', subject_template_name='password_reset_subject.txt'), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    path('summernote/', include('django_summernote.urls')),
    path('setting/password/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html'), name='password_change'),
    path('setting/password/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'), name="password_change_done"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
