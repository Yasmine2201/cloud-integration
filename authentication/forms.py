from django import forms
from django.contrib.auth.forms import UserCreationForm

from authentication.models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',  # This enables the calendar picker
        })
    )
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email','birth_date']