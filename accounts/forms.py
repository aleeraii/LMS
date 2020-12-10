from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(
        max_length=30, required=True, help_text='Required')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'user_role', 'phone_number', 'address', 'password1', 'password2', )


class SignInForm(forms.Form):
    username = forms.CharField(label='username', max_length=300, required=True)
    password = forms.CharField(
        widget=forms.PasswordInput, label='Password', required=True)
