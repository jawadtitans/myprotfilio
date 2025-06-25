# forms.py contains forms for authentication and user management.
from django import forms
from .models import User

# Userform is used for user registration and profile editing.

class Userform(forms.ModelForm):
    role = forms.ChoiceField(
        choices=User.role_choices,
        required=True,
        label='',
        widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Role'})
    )
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'role', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', }),
            'last_name': forms.TextInput(attrs={'class': 'form-input', }),
            'username': forms.TextInput(attrs={'class': 'form-input', }),
            'email': forms.EmailInput(attrs={'class': 'form-input', }),
            'phone_number': forms.TextInput(attrs={'class': 'form-input', }),
            'password': forms.PasswordInput(attrs={'class': 'form-input password-input',}),
        }

# LoginForm supports role-based login: [email - password] => for admin, [Application-ID/QR/ - password] for instructor/student.
# TODO: Implement QR code parsing in the form if needed in the future.
class LoginForm(forms.Form):
    identifier = forms.CharField(label='Email or ID/Username or QR', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        identifier = cleaned_data.get('identifier')
        password = cleaned_data.get('password')
        if not identifier or not password:
            raise forms.ValidationError('Both fields are required.')
        return cleaned_data