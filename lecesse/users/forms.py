from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        exclude = ['id','last_login','username' ,'is_staff', 'is_superuser','user_permissions','is_active','date_joined']
        fields = ['first_name', 'last_name' ,'document_number','email', 'phone_number', 'address','password1', 'role', ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'document_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Document Number'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'role': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Role'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }
        labels = {
            'first_name': ('First Name'),
            'last_name': ('Last Name'),
            'document_number': ('Number Document'),
            'phone_number': ('Number Phone'),
            'email': ('E-Mail'),
            'address': ('Address'),
            'role': ('Role'),
            'project': ('Project'),
            'password1': ('Password'),
        }
        help_texts = {
            'username': '',
            'is_active': '',
            'is_staff': '',
            'groups': '',
        }
    def clean_email(self):
        data = self.cleaned_data['email']
        return data.lower()


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        exclude = ['id', 'last_login', 'username', 'is_staff', 'is_superuser', 'user_permissions', 'is_active',
                   'date_joined']
        fields = ['first_name', 'last_name', 'document_number', 'email', 'phone_number', 'address', 'role',
                  ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'document_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': ('First Name'),
            'last_name': ('Last Name'),
            'document_number': ('Number Document'),
            'phone_number': ('Number Phone'),
            'email': ('E-Mail'),
            'address': ('Address'),
            'role': ('Role'),
        }
        help_texts = {
            'username': '',
            'is_active': '',
            'is_staff': '',
            'groups': '',
        }

    def clean_email(self):
        data = self.cleaned_data['email']
        return data.lower()