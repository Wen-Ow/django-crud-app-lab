import django.forms as forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    email: forms.EmailField(required=True, help_text='Required. Enter a valid email address.')
    first_name: forms.CharField(max_length=30, required=True, help_text='Required. Enter your first name.')
    last_name: forms.CharField(max_length=30, required=True, help_text='Required. Enter your last name.')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')