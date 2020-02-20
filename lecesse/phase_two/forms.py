from django import forms
from .models import *

class EnvironmentsForm(forms.ModelForm):
    class Meta:
        model = Environment
        fields = ['name', 'description','measured_type','area_total','icon']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Description'}),
            'measured_type': forms.Select(attrs={'class': 'form-control','placeholder': 'Measured Type'}),
            'area_total': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Area'})
        }
        labels = {
            'name': ('Name '),
            'description': ('Description'),
            'area_total': ('Area'),
        }


class Environments_Edit_Form(forms.ModelForm):
    class Meta:
        model = Environment
        fields = ['name', 'description', 'measured_type', 'area_total', 'icon']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'measured_type': forms.Select(attrs={'class': 'form-control'}),
            'area_total': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'name': ('Name '),
            'description': ('Description'),
            'area_total': ('Area'),
        }


class Model_Apto_Form(forms.ModelForm):
    class Meta:
        model = Apto_Model
        fields = ['name', 'identifier','flat','cover_page']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'identifier': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Identifier'}),
        }
        labels = {
            'name': ('Name '),
            'description': ('Description')
        }


class Edit_Model_Apto_Form(forms.ModelForm):
    class Meta:
        model = Apto_Model
        fields = ['name', 'identifier','flat','cover_page']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'identifier': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Identifier'}),
        }
        labels = {
            'name': ('Name '),
            'description': ('Description')
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name_project','address','city','state','zip_code',
                  'owner_project']
        widgets = {
            'name_project': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name_project': ('Name'),
            'address': ('Address'),
            'city': ('City'),
            'state': ('State'),
            'zip_code': ('Zip Code'),
            'owner_project': ('Owner Project')
        }


class Project_Edit_Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name_project', 'address', 'city', 'state', 'zip_code',
                  'owner_project']
        widgets = {
            'name_project': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_project': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name_project': ('Name'),
            'address': ('Address'),
            'city': ('City'),
            'state': ('State'),
            'zip_code': ('Zip Code'),
            'owner_project': ('Owner Project'),
        }